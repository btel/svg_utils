from svgutils.compose import *
from nose.tools import ok_
from svgutils.transform import SVG, XLINK
import codecs
import hashlib

def test_embedded_image():
    lion_jpg_md5 = 'f4a7c2a05f2acefa50cbd75a32d2733c'

    fig = Figure("5cm", "5cm",
                 Image(120, 120,
                       'examples/files/lion.jpeg')
                 )
    image = fig.root.find(SVG+'image')
    image_data = image.attrib[XLINK+'href']
    image_data = image_data.replace('data:image/jpeg;base64,', '').encode('ascii')
    base64 = codecs.decode(image_data, 'base64')
    md5 = hashlib.md5(base64).hexdigest()

    ok_(lion_jpg_md5 == md5)

def test_text():

    fig = Figure("5cm", "5cm",
                 Text('lion')
                 )
    txt = fig.root.find(SVG+'text')

    ok_(txt.text=='lion')

def test_no_unit():
    """no unit defaults to px"""

    no_unit = Unit(10)
    assert no_unit.unit == 'px'
    assert no_unit.value == 10.

def test_units():
    """test unit parsing"""

    length = Unit("10cm")
    assert length.unit == 'cm'
    assert length.value == 10

    length = Unit("10.5cm")
    assert length.unit == 'cm'
    assert length.value == 10.5
