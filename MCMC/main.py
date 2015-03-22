import prettyplotlib as pplt
from metrohasting import *
import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt

rcParams['font.size'] = 18
rcParams['figure.figsize'] = (10, 6)

# define our starting point
w_0 = np.array([0., 1., 1., 1., 1., 1., 1., 1., 1., 1.])

# actually do the sampling
n = 5000
samples = metropolis(w_0, n)
v = samples[0, :]

fig, (ax0, ax1) = plt.subplots(2, 1)

# show values of sampled v by iteration
pplt.plot(ax0, np.arange(n), v)
ax0.set_xlabel('iteration number')
ax0.set_ylabel('value of sampled v')

# plot a histogram of values of v
pplt.hist(ax1, v, bins=80)
ax1.set_xlabel('values of sampled v')
ax1.set_ylabel('observations')

plt.tight_layout()
