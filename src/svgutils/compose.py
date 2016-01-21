#!/usr/bin/env python
# coding=utf-8
"""SVG definitions designed for easy SVG composing

Features:
    * allow for wildcard import
    * defines a mini language for SVG composing
    * short but readable names
    * easy nesting
    * method chaining
    * no boilerplate code (reading files, extracting objects from svg,
                           transversing XML tree)
    * universal methods applicable to all element types
    * dont have to learn python

ToDo:
    * emebed images (JPEG, PNG etc.)
"""

import os
import re

from svgutils import transform as _transform
CONFIG = {'svg.file_path': '.',
          'image.file_path': '.',
          'text.position': (0, 0),
          'text.size': 8,
          'text.weight': 'normal',
          'text.font': 'Verdana'}


class Element(_transform.FigureElement):
    """Base class for new SVG elements."""

    def scale(self, factor):
        """Scale SVG element.

        Arguments
        ---------
        factor : float
            The scaling factor.

            Factor > 1 scales up, factor < 1 scales down.
        """

        self.moveto(0, 0, factor)
        return self

    def move(self, x, y):
        self.moveto(x, y, 1)
        return self

    def find_id(self, element_id):
        element = _transform.FigureElement.find_id(self, element_id)
        return Element(element.root)

    def find_ids(self, element_ids):
        elements = [_transform.FigureElement.find_id(self, eid)
                    for eid in element_ids]
        return Panel(*elements)


class SVG(Element):
    """Insert SVG from file.

    Arguments
    ---------
    fname : str
       name of the file
    """

    def __init__(self, fname):
        fname = os.path.join(CONFIG['svg.file_path'], fname)
        svg = _transform.fromfile(fname)
        self.root = svg.getroot().root


class Image(Element):

    def __init__(self, width, height, fname):
        fname = os.path.join(CONFIG['image.file_path'], fname)
        _, fmt = os.path.splitext(fname)
        fmt = fmt.lower()[1:]
        with open(fname, 'rb') as fid:
            img = _transform.ImageElement(fid, width, height, fmt)
        self.root = img.root


class Text(Element):
    def __init__(self, text, x=None, y=None, **kwargs):
        params = {'size': CONFIG['text.size'],
                  'weight': CONFIG['text.weight'],
                  'font': CONFIG['text.font']}
        if x is None or y is None:
            x, y = CONFIG['text.position']
        params.update(kwargs)
        element = _transform.TextElement(x, y, text, **params)
        Element.__init__(self, element.root)


class Panel(Element):
    def __init__(self, *svgelements):
        element = _transform.GroupElement(svgelements)
        Element.__init__(self, element.root)

    def __iter__(self):
        elements = self.root.getchildren()
        return (Element(el) for el in elements)


class Line(Element):
    def __init__(self, points, width=1, color='black'):
        element = _transform.LineElement(points, width=width, color=color)
        Element.__init__(self, element.root)


class Grid(Element):
    def __init__(self, dx, dy, size=8):
        self.size = size
        lines = self._gen_grid(dx, dy)
        element = _transform.GroupElement(lines)
        Element.__init__(self, element.root)

    def _gen_grid(self, dx, dy, width=0.5):
        xmax, ymax = 1000, 1000
        x, y = 0, 0
        lines = []
        txt = []
        while x < xmax:
            lines.append(_transform.LineElement([(x, 0), (x, ymax)],
                                                width=width))
            txt.append(_transform.TextElement(x, dy/2, str(x), size=self.size))
            x += dx
        while y < ymax:
            lines.append(_transform.LineElement([(0, y), (xmax, y)],
                                                width=width))
            txt.append(_transform.TextElement(0, y, str(y), size=self.size))
            y += dy
        return lines+txt


class Figure(Panel):
    def __init__(self, width, height, *svgelements):
        Panel.__init__(self, *svgelements)
        self.width = Unit(width)
        self.height = Unit(height)

    def save(self, fname):
        element = _transform.SVGFigure(self.width, self.height)
        element.append(self)
        element.save(fname)

    def tile(self, ncols, nrows):
        dx = (self.width/ncols).to('px').value
        dy = (self.height/nrows).to('px').value
        ix, iy = 0, 0
        for el in self:
            el.move(dx*ix, dy*iy)
            ix += 1
            if ix >= ncols:
                ix = 0
                iy += 1
            if iy > nrows:
                break
        return self


class Unit:
    per_inch = {'px': 90,
                'cm': 2.54}

    def __init__(self, measure):
        m = re.match('([0-9]+)([a-z]+)', measure)
        value, unit = m.groups()
        self.value = float(value)
        self.unit = unit

    def to(self, unit):
        u = Unit("0cm")
        u.value = self.value/self.per_inch[self.unit]*self.per_inch[unit]
        u.unit = unit
        return u

    def __str__(self):
        return "{}{}".format(self.value, self.unit)

    def __mul__(self, number):
        u = Unit("0cm")
        u.value = self.value * number
        u.unit = self.unit
        return u

    def __div__(self, number):
        return self * (1./number)
