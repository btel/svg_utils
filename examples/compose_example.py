#!/usr/bin/env python
#coding=utf-8

from svgutils.compose import *

CONFIG['svg.file_path'] = 'files'
CONFIG['image.file_path'] = 'files'

Figure( "10cm", "5cm",
        SVG('svg_logo.svg').scale(0.2),
        Image(120, 120, 
            'lion.jpeg', 
        ).move(120, 0)
).save('test.svg')
