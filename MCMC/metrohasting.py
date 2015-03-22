from __future__ import division

import numpy as np
import scipy.stats as ss


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











def metropolis(init, iters):
    """
    based on http://www.cs.toronto.edu/~asamir/cifar/rpa-tutorial.pdf
    
    can take several minutes to run with large sample sizes.
    """
    dist = joint_dist()

    # set up empty sample holder
    D = len(init)
    samples = np.zeros((D, iters))

    # initialize state and log-likelihood
    state = init.copy()
    Lp_state = dist.loglike(state)

    accepts = 0
    for i in np.arange(0, iters):
        
        # propose a new state
        prop = np.random.multivariate_normal(state.ravel(), np.eye(10)).reshape(D, 1)

        Lp_prop = dist.loglike(prop)
        rand = np.random.rand()
        if np.log(rand) < (Lp_prop - Lp_state):
            accepts += 1
            state = prop.copy()
            Lp_state = Lp_prop

        samples[:, i] = state.copy().ravel()
        
        # if i % 1000 == 0: print i

    print 'Acceptance ratio', accepts/iters
    return samples
