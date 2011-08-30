Python-based SVG editor
=======================

This is an utility package that helps to edit and concatenate SVG
files. It is especially directed at scientists preparing final figures
for submission to journal. So far it supports arbitrary placement and
scaling of svg figures and adding markers, such as labels.

See a `blog post <http://neuroscience.telenczuk.pl/?p=331>`_  for a short tutorial.

Install
-------

To install system-wide (needs administrator privilages)::

   python setup.py install

To install locally (do not forget to add
``$HOME/python/lib/python2.6/site-packages/`` to your Python path):

   python setup.py install --user

License
-------

The package is distributed under MIT license (see LICENSE file for
information).

Related packages
----------------

`svg_stack <https://github.com/astraw/svg_stack>`_ is a similar
package that layouts multiple SVG files automatically (in a Qt-style).

Authors
-------

Bartosz Telenczuk (bartosz.telenczuk@gmail.com)
