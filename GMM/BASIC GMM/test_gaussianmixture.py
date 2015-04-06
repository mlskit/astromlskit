import numpy as np
import gaussianmixture

def _sq(x):
    return x*x

def test_gm():
    j= np.random.seed()
    print j
    centroids = np.repeat(np.arange(4), 4).reshape((4,4))
    #print centroids
    fmatrix = np.concatenate([(np.random.randn(12,4)+c) for c in centroids])
    #print fmatrix
    assignments = np.repeat(np.arange(4), 12)
    print assignments
    rss = sum(np.sum(_sq(fmatrix[i*12:(i+1)*12]-i)) for i in xrange(4))
    print rss
    assert np.abs(gaussianmixture.residual_sum_squares(fmatrix, assignments, centroids) - rss) < 1.e-12
    assert gaussianmixture.BIC(fmatrix, assignments, centroids) > 0
    assert gaussianmixture.AIC(fmatrix, assignments, centroids) > 0

    print gaussianmixture.BIC(fmatrix, assignments, centroids, model='full_covariance') > \
        gaussianmixture.BIC(fmatrix, assignments, centroids, model='diagonal_covariance') > \
        gaussianmixture.BIC(fmatrix, assignments, centroids, model='one_variance')

    print gaussianmixture.AIC(fmatrix, assignments, centroids, model='full_covariance') > \
        gaussianmixture.AIC(fmatrix, assignments, centroids, model='diagonal_covariance') > \
        gaussianmixture.AIC(fmatrix, assignments, centroids, model='one_variance')

test_gm()
