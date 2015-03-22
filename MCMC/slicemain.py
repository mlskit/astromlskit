# define our starting point
w_0 = np.array([0., 1., 1., 1., 1., 1., 1., 1., 1., 1.])

# actually do the sampling
n = 10000
sigma = np.ones(10)
samples = slice_sample(w_0, iters=n, sigma=sigma)
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

plt.tight_layout(
