#!/usr/bin/env python3
# coding=utf-8

from svgutils import transform

fig = transform.SVGFigure("100px", "40px")

txt1 = transform.TextElement("0", "10", "ABCDEFGHIJ", size=12)
txt2 = transform.TextElement("0", "20", "ABCDEFGHIJ", size=12, letterspacing=1)
txt3 = transform.TextElement("0", "30", "ABCDEFGHIJ", size=12, letterspacing=2)
txt4 = transform.TextElement("0", "40", "ABCDEFGHIJ", size=12, letterspacing=-1)

fig.append([txt1, txt2, txt3, txt4])
fig.save("letterspacing.svg")
