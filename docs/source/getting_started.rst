.. title:: svgutils tutorial

=====================================
Getting Started
=====================================

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
