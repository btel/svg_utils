.. title:: svgutils tutorial

=====================================
Creating publication-quality figures
=====================================

`Matplotlib <http://matplotlib.sf.net>`_ is a decent Python library
for creating publication-quality plots which offers a multitude of
different plot types. However, one limitation of ``matplotlib`` is that
creating complex layouts can be at times complicated. Therefore,
post-processing of plots is usually done in some other vector graphics
editor such as `inkscape <http://inkscape.org/>`_ or Adobe
Illustrator. The typical workflow is as following:

1. Import and analyse data in Python
#. Create figures in ``matplotlib``
#. Export  figures to PDF/SVG
#. Import figures to vector-graphics editor
#. Arrange and edit figures manually
#. Export the figure to PDF

As you probably see, the typical workflow is quite complicated. To
make things worse you may need to repeat the process several times,
when, for example, you want to include more data into the analysis.
This includes manual editing  and arranging the figure, which is
obviously time consuming.  Therefore it makes sense to try and
automate the process. A description of an automatic workflow
which completely resides on Python tools is given here.

1. *Creating Matplotlib plots*

   To create nice matplotlib-based plots so as 
   to compose figures from. Download
   the following example scripts:
   `anscombe.py <https://github.com/btel/svg_utils/raw/master/docs/source/tutorial/anscombe.py>`_ and `sigmoid_fit.py <https://github.com/btel/svg_utils/raw/master/docs/source/tutorial/sigmoid_fit.py>`_.

   .. figure:: figures/sigmoid_fit.png
      :scale: 20 %

      ``sigmoid_fit.py``

   .. figure:: figures/anscombe.png
      :scale: 70 %

      ``anscombe.py``

2. *Exporting to SVG*

   A nice feature of matplotlib is that one can export figures to
   Scalable Vector Graphics (SVG) which is an open  vector format [1]_
   understood by many applications (such as Inkscape, Adobe
   Illustrator or even web browsers). In a nutshell, SVG files are text files with special
   predefined tags (similar to HTML tags). One can open it in a text editor too.

3. *Arranging plots into composite figures*
   
   Using ``svgutils``, one can combine both plots into one figure and add
   some annotations (such as one-letter labels: A,B, etc.). Download ``svgutils`` from `github
   <https://github.com/btel/svg_utils>`_.

   The basic operations are similar to what one would do in a vector
   graphics editor but using scripts instead of a mouse cursor. This reduces repitition as one will not have to repeat the process when,
   for some reason, one needs to modify the plots they generated
   with matplotlib (to add more data or modify the
   parameters to the analysis, for example).

   An example script is shown and explained below:

.. _transform-example-code:

   .. literalinclude:: scripts/fig_final.py

4. *Convert to PDF/PNG*

   After running the script, one can convert the output file to a
   format of their choice. For this, we suggest using ``inkscape`` which
   can produce PNG and PDF files from SVG source. 
   One can do that directly from command line without the need of opening the whole application::

      inkscape --export-pdf=fig_final.pdf fig_final.svg
      inkscape --export-png=fig_final.png fig_final.svg

   And here is the final result:

   .. figure:: figures/fig_final.png

      Final publication-ready figure.

If one wishes to re-do the plots, they can simply re-run the
above scripts. Automation of the process by means of a build
system, such as GNU ``make`` or similar is also an option. This part will be covered in
some of the next tutorials from the series.

Good luck and happy plotting!


.. [1] A vector format in contrast to other
   (raster) formats such as PNG, JPEG does not represent graphics as
   individual pixels, but rather as modifiable objects (lines, circles,
   points etc.). They usually offer better qualitiy for publication plots
   (PDF files are one of them) and are also editable.
