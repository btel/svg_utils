``compose`` -- easy figure composing
------------------------------------

``compose`` module is a wrapper on top of :py:mod:`svgutils.transform` that
simplifies composing SVG figures. Here is a short example of how a figure could
be constructed::

    Figure( "10cm", "5cm",
            SVG('svg_logo.svg').scale(0.2),
            Image(120, 120, 'lion.jpeg').move(120, 0)
          ).save('test.svg')

.. automodule:: svgutils.compose
   :members:
