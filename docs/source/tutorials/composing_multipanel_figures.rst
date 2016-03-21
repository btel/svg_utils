Composing multi-panel figures
=============================

As I already explained in the previous tutorial, creating figures
programmatically has many advantages. However, obtaining a complex
layout only by scripting can be very time consuming and even 
distressing. Therefore, the possible gains can be crippled by the
time spent tweaking the programs to obtain optimal results and under
time pressure many of us resort to visual editors. One way to alleviate
the problem is to use a library with little boilerplate code and which 
simplifies the common tasks (such as inserting a new panel and adjusting
its position). That's why I introduced the :doc:`compose` module, which
is a wrapper around the low-level API described in :doc:`publication_quality_figures`.

Let's take the example from the previous tutorial

.. figure:: fig_final.png

To obtain this nicely-formatted final figure we needed a considerable amount of code. 
The same effect could be achieved in ``compose`` with much fewer lines::


