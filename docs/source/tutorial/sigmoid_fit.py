from matplotlib import rcParams

#set plot attributes
fig_width = 5  # width in inches
fig_height = 3  # height in inches
fig_size =  [fig_width,fig_height]
params = {'backend': 'Agg',
          'axes.labelsize': 8,
          'axes.titlesize': 8,
          'font.size': 8,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'figure.figsize': fig_size,
          'savefig.dpi' : 600,
          'font.family': 'sans-serif',
          'axes.linewidth' : 0.5,
          'xtick.major.size' : 2,
          'ytick.major.size' : 2,
          'font.size' : 8
          }
rcParams.update(params)


import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1./(1+np.exp(-(x-5)))+1

np.random.seed(1234)
t = np.arange(0.1, 9.2, 0.15)
y = sigmoid(t) + 0.2*np.random.randn(len(t))
residuals = y - sigmoid(t)

t_fitted = np.linspace(0, 10, 100)

#adjust subplots position
fig = plt.figure()

ax1 = plt.axes((0.18, 0.20, 0.55, 0.65))
plt.plot(t, y, 'k.', ms=4., clip_on=False)
plt.plot(t_fitted, sigmoid(t_fitted), 'r-', lw=0.8)

plt.text(5, 1.0, r"L = $\frac{1}{1+\exp(-V+5)}+10$",
                   fontsize=10,
                   transform=ax1.transData, clip_on=False,
                   va='top', ha='left')

#set axis limits
ax1.set_xlim((t.min(), t.max()))
ax1.set_ylim((y.min(), y.max()))

#hide right and top axes
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_position(('outward', 20))
ax1.spines['left'].set_position(('outward', 30))
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')

#set labels
plt.xlabel(r'voltage (V, $\mu$V)')
plt.ylabel('luminescence (L)')

#make inset
ax_inset = plt.axes((0.2, 0.75, 0.2, 0.2), frameon=False)
plt.hist(residuals, fc='0.8',ec='w', lw=2)
plt.xticks([-0.5, 0, 0.5],[-0.5, 0, 0.5], size=6)
plt.xlim((-0.5, 0.5))
plt.yticks([5, 10], size=6)
plt.xlabel("residuals", size=6)
ax_inset.xaxis.set_ticks_position("none")
ax_inset.yaxis.set_ticks_position("left")
#plt.hlines([0, 5, 10],-0.6,0.6, lw=1, color='w')
ax_inset.yaxis.grid(lw=1, color='w', ls='-')
plt.text(0, 0.9, "frequency", transform=ax_inset.transAxes,
        va='center', ha='right', size=6
    )
#export to svg
plt.savefig('sigmoid_fit.png')
plt.savefig('sigmoid_fit.svg')
