from __future__ import division

import numpy as np
import scipy.stats as ss
import prettyplotlib as pplt
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['font.size'] = 18
rcParams['figure.figsize'] = (10, 6)

class joint_dist(object):

    def rvs(self, n=1):
        """ sample a random variable from this distribution """
        sample = np.zeros((10, n))

        for i in xrange(n):
            # generate rvs
            v = ss.norm(0, 3).rvs()
            xs = ss.norm(0, np.sqrt(np.e**v)).rvs(9)
            # place in sample array
            sample[0, i] = v
            sample[1:, i] = xs

        return sample

    def pdf(self, sample):
        """ get the probability of a specific sample """
        v = sample[0]
        pv = ss.norm(0, 3).pdf(v)
        xs = sample[1:]
        pxs = [ss.norm(0, np.sqrt(np.e**v)).pdf(x_k) for x_k in xs]
        return np.array([pv] + pxs)

    def loglike(self, sample):
        """ log likelihood of a specific sample """
        return np.sum(np.log(self.pdf(sample)))



def slice_sample(init, iters, sigma, step_out=True):
    """
    based on http://homepages.inf.ed.ac.uk/imurray2/teaching/09mlss/
    """

    dist = joint_dist()

    # set up empty sample holder
    D = len(init)
    samples = np.zeros((D, iters))

    # initialize
    xx = init.copy()

    for i in xrange(iters):
        perm = range(D)
        np.random.shuffle(perm)
        last_llh = dist.loglike(xx)

        for d in perm:
            llh0 = last_llh + np.log(np.random.rand())
            rr = np.random.rand(1)
            x_l = xx.copy()
            x_l[d] = x_l[d] - rr * sigma[d]
            x_r = xx.copy()
            x_r[d] = x_r[d] + (1 - rr) * sigma[d]

            if step_out:
                llh_l = dist.loglike(x_l)
                while llh_l > llh0:
                    x_l[d] = x_l[d] - sigma[d]
                    llh_l = dist.loglike(x_l)
                llh_r = dist.loglike(x_r)
                while llh_r > llh0:
                    x_r[d] = x_r[d] + sigma[d]
                    llh_r = dist.loglike(x_r)

            x_cur = xx.copy()
            while True:
                xd = np.random.rand() * (x_r[d] - x_l[d]) + x_l[d]
                x_cur[d] = xd.copy()
                last_llh = dist.loglike(x_cur)
                if last_llh > llh0:
                    xx[d] = xd.copy()
                    break
                elif xd > xx[d]:
                    x_r[d] = xd
                elif xd < xx[d]:
                    x_l[d] = xd
                else:
                    raise RuntimeError('Slice sampler shrank too far.')

        if i % 1000 == 0: print 'iteration', i

        samples[:, i] = xx.copy().ravel()

    return samples


w_0 = np.array([0., 1., 1., 1., 1., 1., 1., 1., 1., 1.])

# actually do the sampling
n = 10
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

plt.tight_layout()
plt.show()
