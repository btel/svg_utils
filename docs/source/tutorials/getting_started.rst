.. title:: svgutils tutorial

=====================================
Getting Started
=====================================

Install
-------

From PyPI
`````````

You can install `svgutils` from Python Package Index (PyPI) using the `pip` utility::

   pip install svgutils --user

Note that the `pip` will attempt to install `lxml` library if it is not already installed.
For the installation to be sucessful, you need development libraries of `libxml2` and `libxslt1`.
On Ubuntu and other Debian-derived Linux distributions you can install them via::

   sudo apt-get install libxml2-dev libxslt-dev
   
From Conda
``````````
Installing `svgutils` from the `conda-forge` channel can be achieved by adding `conda-forge` to your channels with::

    conda config --add channels conda-forge
    
You can install `svgutils` from `conda-forge` channel::

   conda install svgutils

From sources
````````````

To install system-wide (needs administrator privilages)::

   python setup.py install

To install locally (do not forget to add
``$HOME/python/lib/python2.6/site-packages/`` to your Python path)::

   python setup.py install --user
