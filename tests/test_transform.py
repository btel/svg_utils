#!/usr/bin/env python
#coding=utf-8

from svgutils import transform
from nose.tools import ok_

circle = """<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="150" height="50" class='main'>
  <circle cx="100" cy="50" r="40" stroke="black"
  stroke-width="2" fill="red" />
</svg> 
"""

def test_get_size():
    svg_fig = transform.fromstring(circle)
    w, h = svg_fig.get_size()
    ok_((w=='150') & (h=='50'))

def test_group_class():
    svg_fig = transform.fromstring(circle)
    group = svg_fig.getroot()
    ok_((group.root.attrib['class'] == 'main'))

def test_skew():
    svg_fig = transform.fromstring(circle)
    group = svg_fig.getroot()

    # Test skew in y-axis
    group.skew(0, 30)
    ok_('skewY(30' in group.root.get('transform'))

    # Test skew in x-axis
    group.skew(30, 0)
    ok_('skewX(30' in group.root.get('transform'))

def test_scale_xy():
    svg_fig = transform.fromstring(circle)
    group = svg_fig.getroot()

    group.scale_xy(0, 30)
    ok_('scale(0' in group.root.get('transform'))
