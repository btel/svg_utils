#!/usr/bin/env python3
# coding=utf-8

from setuptools import setup

version_str = "0.3.4"

setup(
    name="svgutils",
    version=version_str,
    description="Python SVG editor",
    long_description="""This is an utility package that helps to edit and
      concatenate SVG files. It is especially directed at scientists preparing
      final figures for submission to journal. So far it supports arbitrary
      placement and scaling of svg figures and
      adding markers, such as labels.""",
    author="Bartosz Telenczuk",
    author_email="bartosz.telenczuk@gmail.com",
    url="https://svgutils.readthedocs.io",
    packages=["svgutils"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Graphics :: Editors :: Vector-Based",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Text Processing :: Markup",
    ],
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=["lxml"],
    download_url="https://github.com/btel/svg_utils/archive/v{}.tar.gz".format(
        version_str
    ),
)
