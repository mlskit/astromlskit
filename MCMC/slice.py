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
