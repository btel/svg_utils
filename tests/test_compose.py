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

