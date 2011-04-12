#!/usr/bin/env python
#coding=utf-8

from setuptools import setup

setup(name='svgutils',
      version='0.1',
      description='Python SVG editor',
      author='Bartosz Telenczuk',
      author_email='bartosz.telenczuk@gmail.com',
      url='http://neuroscience.telenczuk.pl',
      packages=['svgutils', 
                ],
      package_dir = {"": "src"},
      install_requires=[
        ]
      
     )

