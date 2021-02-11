#!/usr/bin/env python3
# coding=utf-8

from svgutils.transform import fromfile
from svgutils.templates import VerticalLayout, ColumnLayout


layout = ColumnLayout(5)

for i in range(12):
    svg = fromfile("files/example.svg")
    layout.add_figure(svg)

layout.save("stack_svg.svg")
