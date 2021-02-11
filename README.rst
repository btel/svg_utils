.. image:: https://github.com/btel/svg_utils/workflows/Run%20the%20test%20suite/badge.svg
    :target: https://github.com/btel/svg_utils/actions

.. image:: https://readthedocs.org/projects/svgutils/badge/?version=latest
    :target: http://svgutils.readthedocs.io/en/latest/?badge=latest

Python-based SVG editor
=======================

This is an utility package that helps to edit and concatenate SVG
files. It is especially directed at scientists preparing final figures
for submission to journal. So far it supports arbitrary placement and
scaling of svg figures and adding markers, such as labels.

See the `blog post <http://neuroscience.telenczuk.pl/?p=331>`_  for a short tutorial.

The full documentation is available 
`here <https://svgutils.readthedocs.io/en/latest/index.html>`_.

Install
-------

From PyPI
`````````

You can install `svgutils` from Python Package Index (PyPI) using the `pip3` utility::

   pip3 install svgutils --user

Note that the `pip3` will attempt to install `lxml` library if it is not already installed.
For the installation to be sucessful, you need development libraries of `libxml2` and `libxslt1`.
On Ubuntu and other Debian-derived Linux distributions you can install them via::

   sudo apt-get install libxml2-dev libxslt-dev
   
From Conda
``````````
Installing `svgutils` from the `conda-forge` channel can be achieved by adding `conda-forge` to your channels with::

    conda config --add channels conda-forge
    
You can install `svgutils` from `conda-forge` channel::

   conda install svgutils

If you don't want to add the channel to your configuration, you can specify it at the time of installation::
   
   conda install svgutils -c conda-forge 

From sources
````````````

To install system-wide (needs administrator privilages)::

   python3 setup.py install

To install locally (do not forget to add
``$HOME/python/lib/python3.6/site-packages/`` to your Python path)::

   python3 setup.py install --user

License
-------

The package is distributed under MIT license (see LICENSE file for
information).

Related packages
----------------

`svg_stack <https://github.com/astraw/svg_stack>`_ is a similar
package that layouts multiple SVG files automatically (in a Qt-style).

`svgmanip <https://github.com/CrazyPython/svgmanip>`_ a related
library that aims for a simple API with the ability to export to
PNG accurately

`cairosvg <http://cairosvg.org/>`_ a command-line SVG to PNG converter 
for Python 3.4+

`svglib <https://pypi.python.org/pypi/svglib/>`_ a pure-Python 
library for reading and converting SVG

Authors
-------

Bartosz Telenczuk (bartosz.telenczuk@gmail.com)
