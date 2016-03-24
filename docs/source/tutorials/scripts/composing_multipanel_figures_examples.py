#!/usr/bin/env python
#coding=utf-8
from svgutils.compose import *

CONFIG['figure.save_path'] = 'composing_multipanel_figures'

Figure("16cm", "6.5cm",
       SVG("sigmoid_fit.svg")
       ).save("ex1.svg")

Figure("16cm", "6.5cm", 
        Text("A", 25, 20),
        SVG("sigmoid_fit.svg")
       ).save('ex1a.svg')

Figure("16cm", "6.5cm", 
        Text("A", 25, 20, size=12, weight='bold'),
        SVG("sigmoid_fit.svg")
       ).save('ex1b.svg')

Figure("16cm", "6.5cm", 
      SVG("sigmoid_fit.svg"),
      SVG("anscombe.svg")
      ).save("ex2.svg")

Figure("16cm", "6.5cm", 
       SVG("sigmoid_fit.svg"),
       SVG("anscombe.svg")
       ).tile(2, 1).save("ex3.svg")

Figure("16cm", "6.5cm", 
       SVG("sigmoid_fit.svg"),
       SVG("anscombe.svg").scale(0.5)
       ).tile(2, 1).save("ex3b.svg")

Figure("16cm", "6.5cm", 
        SVG("sigmoid_fit.svg"),
        SVG("anscombe.svg").move(280, 0)
        ).save("ex4.svg")

Figure("16cm", "6.5cm", 
      SVG("sigmoid_fit.svg"),
      SVG("anscombe.svg").scale(0.5)
                         .move(280, 0)
      ).save("ex5.svg")


Figure("16cm", "6.5cm", 
       SVG("sigmoid_fit.svg"),
       SVG("anscombe.svg").scale(0.5)
                          .move(280, 0),
       Grid(20, 20)
       ).save("ex6.svg")


Figure("16cm", "6.5cm", 
       Panel(
          Text("A", 25, 20),
          SVG("sigmoid_fit.svg")
          ),
       Panel(
          Text("B", 25, 20).move(280, 0),
          SVG("anscombe.svg").scale(0.5)
                             .move(280, 0)
          )
       ).save('ex7.svg')


Figure("16cm", "6.5cm", 
       Panel(
          Text("A", 25, 20),
          SVG("sigmoid_fit.svg")
          ),
       Panel(
          Text("B", 25, 20),
          SVG("anscombe.svg").scale(0.5)
          ).move(280, 0)
       ).save('ex8.svg')
