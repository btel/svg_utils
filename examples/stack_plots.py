#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

from svgutils.transform import from_mpl
from svgutils.templates import VerticalLayout

layout = VerticalLayout()

fig1 = plt.figure()
plt.plot([1,2])
fig2 = plt.figure()
plt.plot([2,1])

layout.add_figure(from_mpl(fig1))
layout.add_figure(from_mpl(fig2))

print from_mpl(fig1).get_size()
layout.save('stack_plots.svg')

