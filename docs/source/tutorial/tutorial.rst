===================================================================
Creating plublication-quality figures using matplotlib and svgutils
===================================================================

`Matplotlib <http://matplotlib.sf.net>`_ is a decent Python library
for creating publication-quality plots which offers a multitude of
different plot types. However, one limitation of ``matplotlib`` is that
creating complex layouts can be at times complicated. Therefore, the
post-processing of the plots is usually done in some vector graphics
editor such as `inkscape <http://inkscape.org/>`_ or Adobe
Illustrator. The typical workflow is as following:

1. Import and analyse data in Python
#. Create figures in ``matplotlib``
#. Export  figures to PDF/SVG
#. Import figures to vector-graphics editor
#. Arrange and edit figures manually
#. Export the figure to PDF

As you probably see, the workflow may be at time very complicated. To
make things worse you may need to repeat the process several time,
when, for example, you want to include more data into the analysis.
This includes manual editting  and arranging the figure, which is
obviously time consuming.  Therefore it makes sense to try and
automatise the process. Here, I will describe an automatic workflow
which completely resides on Python tools.

1. *Create plots*

   First you need to create nice matplotlib-based plots you would like
   to compose your figure from. You may download
   the scripts I will use in the example from ...

   .. image:: sigmoid_fit.png
      :scale: 10 %

   .. figure:: anscombe.png
      :scale: 1
      
      anscombe.svg

2. *Export to SVG*

   A nice feature of matplotlib is that it allows to export figure to
   Scalable Vector Graphics (SVG) which is an open  vector format [1]_
   understood by many applications (such as Inkscape, Adobe
   Illustrator or even web browsers). Not going to much into details,
   I will only say that SVG files are normal text files with a special
   predefined tags (much alike HTML files). You may try to open one of
   them in a text editor to find out what I mean.

3. *Arange plots into composite figures*

   Now, we would like to combine both plots into one figure and add
   some annotations (such as one-letter labels: A,B, etc.). To this
   end, I will use a Python package I wrote with this purpose
   ``svgutils``. It is written completely in Python and uses only
   standard libraries. You may download it from `github
   <https://github.com/btel/svg_utils>`_.

   The basic operations are similar to what you would do in a vector
   graphics editor, but instead of using a mouse you will do some
   scriptting. It may take some more time at the beginning, but with
   the advantage that you would not have to repeat the process, when
   for some reason you would like to modify the plots you generated
   with matplotlib (you may need to add more data or modify the
   paramters of your analysis, just to name a few reasons).

   An example script is shown below:

   .. literalinclude:: fig_final.py

4. *Convert to PDF/PNG*

   After running the script, you may now convert the output file to a
   format of choice. To this end, you can use ``inkscape`` which can
   produce PNG and PDF file. You can do that directly from command
   line without the need of openning the GUI::

      inkscape --export-pdf=fig_final.pdf fig_final.svg
      inkscape --export-png=fig_final.png fig_final.svg

Now, whenever you need to re-do the plots you can simply re-run the
above scripts. You can also automate the process by means of a build
system, such as GNU ``make`` or similar. This part will be covered in
some of the next tutorials from the series.

Good luck and happy plotting!

.. [1] In case you do not know it, a vector format in contrast to other
   (raster) formats such as PNG, JPEG does not represent graphics as
   individual pixels, but rather as modifiable objects (lines, circles,
   points etc.). They usually offer better qualitiy for publication plots
   (PDF files are one of them) and are also editable.
