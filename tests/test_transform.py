#!/usr/bin/env python
#coding=utf-8

from svgutils import transform
from nose.tools import ok_

def test_get_size():
    svg_fig = transform.fromfile('circle.svg')
    w, h = svg_fig.get_size()
    ok_((w=='150') & (h=='50'))


