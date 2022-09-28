#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

from svgutils.templates import VerticalLayout
from svgutils.transform import from_mpl

layout = VerticalLayout()

fig1 = plt.figure()
plt.plot([1, 2])
fig2 = plt.figure()
plt.plot([2, 1])

layout.add_figure(from_mpl(fig1))
layout.add_figure(from_mpl(fig2))

layout.save("stack_plots.svg")
