#!/usr/bin/env python
#coding=utf-8

from transform import SVGFigure, GroupElement

class BaseTemplate(SVGFigure):

    def __init__(self):
        SVGFigure.__init__(self)
        self.figures = []

    def add_figure(self, fig):
        w, h =  fig.get_size()
        root = fig.getroot()
        self.figures.append({'root': root,
                             'width': w,
                             'height' : h})

    def _transform(self):
        pass

    def save(self, fname):
        self._generate_layout()
        SVGFigure.save(self, fname)

    def _generate_layout(self):
        
        for i,f in enumerate(self.figures):
            new_element = self._transform(f['root'], self.figures[:i])
            self.append(new_element)

class VerticalLayout(BaseTemplate):

    def _transform(self, element, transform_list):
        for t in transform_list:
            element = GroupElement([element])
            element.moveto(0, t['height'])
        return element

class ColumnLayout(BaseTemplate):

    def __init__(self, nrows, row_height=None, col_width=None):
        """Multiple column layout with nrows and required number of
        columns. col_width
        determines the width of the column (defaults to width of the
        first added element)"""

        self.nrows = nrows
        self.col_width = col_width
        self.row_height = row_height

        BaseTemplate.__init__(self)

    def _transform(self, element, transform_list):

        rows = 0
  
        if not transform_list:
            return element

        n_elements = len(transform_list)
        rows = n_elements % self.nrows
        cols = int(n_elements/self.nrows)
        
        if self.col_width is None:
            self.col_width = transform_list[0]['width']
        if self.row_height is None:
            self.row_height = transform_list[0]['height']

        for i in range(rows):
            element = GroupElement([element])
            element.moveto(0, self.row_height)
        
        for i in range(cols):
            element = GroupElement([element])
            element.moveto(self.col_width, 0)

        return element



