#!/usr/bin/env python3
# coding=utf-8

from svgutils.templates import ColumnLayout, VerticalLayout
from svgutils.transform import fromfile

layout = ColumnLayout(5)

for i in range(12):
    svg = fromfile("files/example.svg")
    layout.add_figure(svg)

layout.save("stack_svg.svg")
