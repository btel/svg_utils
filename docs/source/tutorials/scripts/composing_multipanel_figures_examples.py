#!/usr/bin/env python
#coding=utf-8
from svgutils.compose import *

Figure("16cm", "6.5cm",
       SVG("sigmoid_fit.svg")
       ).save("composing_multipanel_figures_ex1.svg")

Figure("16cm", "6.5cm", 
       SVG("sigmoid_fit.svg"),
       SVG("anscombe.svg").scale(0.5)
       ).tile(2, 1).save("composing_multipanel_figures_ex2.svg")

