#!/usr/bin/env python3
# coding=utf-8
from tempfile import NamedTemporaryFile

from svgutils import transform
from svgutils.compose import Unit
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
    ok_((w == "150") & (h == "50"))


def test_group_class():
    svg_fig = transform.fromstring(circle)
    group = svg_fig.getroot()
    ok_((group.root.attrib["class"] == "main"))


def test_skew():
    svg_fig = transform.fromstring(circle)
    group = svg_fig.getroot()

    # Test skew in y-axis
    group.skew(0, 30)
    ok_("skewY(30" in group.root.get("transform"))

    # Test skew in x-axis
    group.skew(30, 0)
    ok_("skewX(30" in group.root.get("transform"))


def test_scale_xy():
    svg_fig = transform.fromstring(circle)
    group = svg_fig.getroot()

    group.scale(0, 30)
    ok_("scale(0" in group.root.get("transform"))


def test_create_svg_figure():
    svg_fig = transform.SVGFigure()
    assert "svg" in svg_fig.to_str().decode("ascii")

    svg_fig = transform.SVGFigure(Unit("2px"), Unit("2px"))
    assert "svg" in svg_fig.to_str().decode("ascii")

    svg_fig = transform.SVGFigure(2, 3)
    assert "svg" in svg_fig.to_str().decode("ascii")

    svg_fig = transform.SVGFigure("2", "3")
    assert "svg" in svg_fig.to_str().decode("ascii")


def test_svg_figure_writes_width_height_and_view_box():
    svg_fig = transform.SVGFigure(Unit("400mm"), Unit("300mm"))

    with NamedTemporaryFile() as f1:
        svg_fig.save(f1.name)
        with open(f1.name) as f2:
            written_content = f2.read()

    assert 'width="400.0mm"' in written_content
    assert 'height="300.0mm"' in written_content
    assert 'viewBox="0 0 400.0 300.0"' in written_content

def test_svg_figure__width_height_tostr():

    svg_fig = transform.SVGFigure("400px", "300px")
    assert b'height="300.0px"' in svg_fig.to_str()
    assert b'width="400.0px"' in svg_fig.to_str()
