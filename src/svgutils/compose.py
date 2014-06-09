#!/usr/bin/env python
#coding=utf-8
"""SVG definitions designed for easy SVG composing

Features:
    * allow for wildcard import
    * defines a mini language for SVG composing
    * short but readable names
    * easy nesting
    * method chaining
    * no boilerplate code (reading files, extracting objects from svg, transversing XML tree)
    * universal methods applicable to all element types
    * dont have to learn python

ToDo:
    * emebed images (JPEG, PNG etc.)
"""

from svgutils import transform as _transform
CONFIG = {'svg.file_path' : '.',
          'text.size' : 8,
          'text.weight' : 'normal',
          'text.font' : 'Verdana'}
import os 

class _Element(_transform.FigureElement):
    def scale(self, factor):
        self.moveto(0,0, factor)
        return self
    
    def move(self, x, y):
        self.moveto(x,y,1)
        return self

class SVG(_Element):

    def __init__(self, fname):
        fname = os.path.join(CONFIG['svg.file_path'], fname) 
        svg = _transform.fromfile(fname)
        self.root = svg.getroot().root

class Image(_Element):

    def __init__(self, fname, width, height):
        _, fmt = os.path.splitext(fname)
        fmt = fmt.lower()[1:]
        with open(fname, 'rb') as fid:
            img = _transform.ImageElement(fid, width, height, fmt)
        self.root = img.root

class Text(_Element):
    def __init__(self, text, x, y, **kwargs):
        params = {'size'   : CONFIG['text.size'],
                  'weight' : CONFIG['text.weight'],
                  'font'   : CONFIG['text.font']}
        params.update(kwargs)
        element = _transform.TextElement(x, y, text, **params)
        self.root = element.root

class Panel(_Element):
    def __init__(self, *svgelements):
        element = _transform.GroupElement(svgelements)
        self.root = element.root

class Line(_Element):
    def __init__(self, points, width=1, color='black'):
        element = _transform.LineElement(points, width=width, color=color)
        self.root = element.root

class Grid(_Element):
    def __init__(self, dx, dy, size=8):
        self.size = size
        lines = self._gen_grid(dx, dy)
        element = _transform.GroupElement(lines)
        self.root = element.root

    def _gen_grid(self, dx, dy, width=0.5):
        xmax, ymax = 1000, 1000
        x, y = 0, 0
        lines = []
        txt = []
        while x<xmax:
            lines.append(_transform.LineElement([(x,0),(x,ymax)], width=width))
            txt.append(_transform.TextElement(x, dy/2, str(x), size=self.size))
            x += dx
        while y<ymax:
            lines.append(_transform.LineElement([(0,y),(xmax,y)], width=width))
            txt.append(_transform.TextElement(0, y, str(y), size=self.size))
            y += dy
        return lines+txt

class Figure(Panel):
    def __init__(self, width, height, *svgelements):
        Panel.__init__(self, *svgelements)
        self.width = width
        self.height = height
    def save(self, fname):
        element = _transform.SVGFigure(self.width, self.height)
        element.append(self)
        element.save(fname)


        
