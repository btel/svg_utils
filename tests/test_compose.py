import codecs
import hashlib

from nose.tools import assert_almost_equal, assert_raises, ok_

import svgutils.compose as sc
from svgutils.compose import *
from svgutils.transform import SVG, XLINK


def test_embedded_svg():
    svg = sc.SVG("examples/files/svg_logo.svg")
    fig = sc.Figure("5cm", "5cm", svg)
    poly = fig.root.find(".//{}polygon".format(SVG))

    ok_(poly.get("id") == "V")

    ok_(svg.height is None)
    ok_(svg.width is None)


def test_embedded_image():
    lion_jpg_md5 = "f4a7c2a05f2acefa50cbd75a32d2733c"

    fig = Figure("5cm", "5cm", Image(120, 120, "examples/files/lion.jpeg"))
    image = fig.root.find(SVG + "image")
    image_data = image.attrib[XLINK + "href"]
    image_data = image_data.replace("data:image/jpeg;base64,", "").encode("ascii")
    base64 = codecs.decode(image_data, "base64")
    md5 = hashlib.md5(base64).hexdigest()

    ok_(lion_jpg_md5 == md5)


def test_text():

    fig = Figure("5cm", "5cm", Text("lion"))
    txt = fig.root.find(SVG + "text")

    ok_(txt.text == "lion")


def test_no_unit():
    """no unit defaults to px"""

    no_unit = Unit(10)
    assert no_unit.unit == "px"
    assert no_unit.value == 10.0


def test_units():
    """test unit parsing"""

    length = Unit("10cm")
    assert length.unit == "cm"
    assert length.value == 10

    length = Unit("10.5cm")
    assert length.unit == "cm"
    assert length.value == 10.5

    with assert_raises(ValueError) as cm:
        Unit("x")
    ex = cm.exception
    assert str(ex) == "Could not parse unit in 'x'"


def test_unit_div():
    """test divding a number with unit by a number"""

    length = Unit("10cm")
    shorter_length = length / 2
    assert length.unit == "cm"
    assert_almost_equal(shorter_length.value, 5)

    shorter_length = length / 2.0
    assert length.unit == "cm"
    assert_almost_equal(shorter_length.value, 5.0)
