import math, random, copy,sys
import numpy as np
import pylab as pl

def expectation_maximization(t, nbclusters=2, nbiter=3, normalize=False,\
        epsilon=0.001, monotony=False, datasetinit=True):
    """ 
    Each row of t is an observation, each column is a feature 
    'nbclusters' is the number of seeds and so of clusters
    'nbiter' is the number of iterations
    'epsilon' is the convergence bound/criterium

    Overview of the algorithm:
    -> Draw nbclusters sets of (μ, σ, P_{#cluster}) at random (Gaussian 
       Mixture) [P(Cluster=0) = P_0 = (1/n).∑_{obs} P(Cluster=0|obs)]
    -> Compute P(Cluster|obs) for each obs, this is:
    [E] P(Cluster=0|obs)^t = P(obs|Cluster=0)*P(Cluster=0)^t
    -> Recalculate the mixture parameters with the new estimate
    [M] * P(Cluster=0)^{t+1} = (1/n).∑_{obs} P(Cluster=0|obs)
        * μ^{t+1}_0 = ∑_{obs} obs.P(Cluster=0|obs) / P_0
        * σ^{t+1}_0 = ∑_{obs} P(Cluster=0|obs)(obs-μ^{t+1}_0)^2 / P_0
    -> Compute E_t=∑_{obs} log(P(obs)^t)
       Repeat Steps 2 and 3 until |E_t - E_{t-1}| < ε
    """
    def pnorm(x, m, s):
        """ 
        Compute the multivariate normal distribution with values vector x,
        mean vector m, sigma (variances/covariances) matrix s
        """
        xmt = np.matrix(x-m).transpose()
        for i in xrange(len(s)):
            if s[i,i] <= sys.float_info[3]: # min float
                s[i,i] = sys.float_info[3]
        sinv = np.linalg.inv(s)
        xm = np.matrix(x-m)
        return (2.0*math.pi)**(-len(x)/2.0)*(1.0/math.sqrt(np.linalg.det(s)))\
                *math.exp(-0.5*(xm*sinv*xmt))

    def draw_params():
            if datasetinit:
                tmpmu = np.array([1.0*t[random.uniform(0,nbobs),:]],np.float64)
            else:
                tmpmu = np.array([random.uniform(min_max[f][0], min_max[f][1])\
                        for f in xrange(nbfeatures)], np.float64)
            return {'mu': tmpmu,\
                    'sigma': np.matrix(np.diag(\
                    [(min_max[f][1]-min_max[f][0])/2.0\
                    for f in xrange(nbfeatures)])),\
                    'proba': 1.0/nbclusters}

    nbobs = t.shape[0]
    nbfeatures = t.shape[1]
    min_max = []
    # find xranges for each features
    for f in xrange(nbfeatures):
        min_max.append((t[:,f].min(), t[:,f].max()))
    
    ### Normalization
    if normalize:
        for f in xrange(nbfeatures):
            t[:,f] -= min_max[f][0]
            t[:,f] /= (min_max[f][1]-min_max[f][0])
    min_max = []
    for f in xrange(nbfeatures):
        min_max.append((t[:,f].min(), t[:,f].max()))
    ### /Normalization

    result = {}
    quality = 0.0 # sum of the means of the distances to centroids
    random.seed()
    Pclust = np.ndarray([nbobs,nbclusters], np.float64) # P(clust|obs)
    Px = np.ndarray([nbobs,nbclusters], np.float64) # P(obs|clust)
    # iterate nbiter times searching for the best "quality" clustering
    for iteration in xrange(nbiter):
        ##############################################
        # Step 1: draw nbclusters sets of parameters #
        ##############################################
        params = [draw_params() for c in xrange(nbclusters)]
        old_log_estimate = sys.maxint         # init, not true/real
        log_estimate = sys.maxint/2 + epsilon # init, not true/real
        estimation_round = 0
        # Iterate until convergence (EM is monotone) <=> < epsilon variation
        while (abs(log_estimate - old_log_estimate) > epsilon\
                and (not monotony or log_estimate < old_log_estimate)):
            restart = False
            old_log_estimate = log_estimate
            ########################################################
            # Step 2: compute P(Cluster|obs) for each observations #
            ########################################################
            for o in xrange(nbobs):
                for c in xrange(nbclusters):
                    # Px[o,c] = P(x|c)
                    Px[o,c] = pnorm(t[o,:],\
                            params[c]['mu'], params[c]['sigma'])
            #for o in xrange(nbobs):
            #    Px[o,:] /= math.fsum(Px[o,:])
            for o in xrange(nbobs):
                for c in xrange(nbclusters):
                    # Pclust[o,c] = P(c|x)
                    Pclust[o,c] = Px[o,c]*params[c]['proba']
            #    assert math.fsum(Px[o,:]) >= 0.99 and\
            #            math.fsum(Px[o,:]) <= 1.01
            for o in xrange(nbobs):
                tmpSum = 0.0
                for c in xrange(nbclusters):
                    tmpSum += params[c]['proba']*Px[o,c]
                Pclust[o,:] /= tmpSum
                #assert math.fsum(Pclust[:,c]) >= 0.99 and\
                #        math.fsum(Pclust[:,c]) <= 1.01
            ###########################################################
            # Step 3: update the parameters (sets {mu, sigma, proba}) #
            ###########################################################
            print "iter:", iteration, " estimation#:", estimation_round,\
                    " params:", params
            for c in xrange(nbclusters):
                tmpSum = math.fsum(Pclust[:,c])
                params[c]['proba'] = tmpSum/nbobs
                if params[c]['proba'] <= 1.0/nbobs:           # restart if all
                    restart = True                             # converges to
                    print "Restarting, p:",params[c]['proba'] # one cluster
                    break
                m = np.zeros(nbfeatures, np.float64)
                for o in xrange(nbobs):
                    m += t[o,:]*Pclust[o,c]
                params[c]['mu'] = m/tmpSum
                s = np.matrix(np.diag(np.zeros(nbfeatures, np.float64)))
                for o in xrange(nbobs):
                    s += Pclust[o,c]*(np.matrix(t[o,:]-params[c]['mu']).transpose()*\
                            np.matrix(t[o,:]-params[c]['mu']))
                    #print ">>>> ", t[o,:]-params[c]['mu']
                    #diag = Pclust[o,c]*((t[o,:]-params[c]['mu'])*\
                    #        (t[o,:]-params[c]['mu']).transpose())
                    #print ">>> ", diag
                    #for i in xrange(len(s)) :
                    #    s[i,i] += diag[i]
                params[c]['sigma'] = s/tmpSum
                print "------------------"
                print params[c]['sigma']

            ### Test bound conditions and restart consequently if needed
            if not restart:
                restart = True
                for c in xrange(1,nbclusters):
                    if not np.allclose(params[c]['mu'], params[c-1]['mu'])\
                    or not np.allclose(params[c]['sigma'], params[c-1]['sigma']):
                        restart = False
                        break
            if restart:                # restart if all converges to only
                old_log_estimate = sys.maxint          # init, not true/real
                log_estimate = sys.maxint/2 + epsilon # init, not true/real
                params = [draw_params() for c in xrange(nbclusters)]
                continue
            ### /Test bound conditions and restart

            ####################################
            # Step 4: compute the log estimate #
            ####################################
            log_estimate = math.fsum([math.log(math.fsum(\
                    [Px[o,c]*params[c]['proba'] for c in xrange(nbclusters)]))\
                    for o in xrange(nbobs)])
            print "(EM) old and new log estimate: ",\
                    old_log_estimate, log_estimate
            estimation_round += 1

        # Pick/save the best clustering as the final result
        quality = -log_estimate
        if not quality in result or quality > result['quality']:
            result['quality'] = quality
            result['params'] = copy.deepcopy(params)
            result['clusters'] = [[o for o in xrange(nbobs)\
                    if Px[o,c] == max(Px[o,:])]\
                    for c in xrange(nbclusters)]
    return result


def plot(clusterst, data, title='', gaussians=[], separate_plots=False):
    if clusterst.has_key('name'):
        title = clusterst['name']
    if clusterst.has_key('params'):
        gaussians = clusterst['params']
    clusters = clusterst['clusters']
    if separate_plots:
        ax = pl.subplot(212)
    else:
        ax = pl.subplot(111)
    colors = 'brgcymk'
    for k in range(len(clusters)):
        print ">>>> drawing ", k
        if len(clusters[k]):
            xy = [[data[i,j] for i in clusters[k]]\
                    for j in range(len(data[0]))]
            if len(data[0]) < 3:
                ax.scatter(xy[0], xy[len(data[0])-1],s=20,\
                        c=colors[k % len(colors)],\
                        marker='s', edgecolors='none')
            else:
                # [len(data[0]) * (len(data[0])+1)] / 2 plots
                total = math.sqrt(len(data[0])*(len(data[0])+1.0)/2.0)
                w = int(math.floor(total))
                h = int(math.floor(total+1))
                plotno = 0 
                for i in range(len(data[0])):
                    r = range(i+1, len(data[0]))
                    for j in r:
                        plotno += 1
                        ax = pl.subplot(h, w, plotno)
                        ax.scatter(xy[i], xy[j],s=20,\
                                c=colors[k % len(colors)], marker='s',\
                                edgecolors='none')
                        
    ranges = [min([data[:,i].min() for i in range(data.shape[1])]),\
            max([data[:,i].max() for i in range(data.shape[1])]),\
            min([data[i,:].min() for i in range(data.shape[0])]),\
            max([data[i,:].max() for i in range(data.shape[0])])]
    ax.axis(ranges)
    pl.title(title)

    ### Plot gaussians
    if len(gaussians):
        Z = []
        for g in gaussians:
            delta = (max(ranges) - min(ranges))/1000
            x = pl.arange(ranges[0], ranges[1], delta)
            y = pl.arange(ranges[2], ranges[3], delta)
            X,Y = pl.meshgrid(x, y)
            for i in range(len(g['sigma'])):
                if not g['sigma'][i,i]:                  # to put uncertainty on
                    g['sigma'][i,i] += 1.0/data.shape[0] # perfectly aligned data
            if len(g['sigma']) == 1:
                Z.append(pl.bivariate_normal(X, Y, g['sigma'][0,0],\
                        g['sigma'][0,0], g['mu'][0], g['mu'][0]))
            else:
                Z.append(pl.bivariate_normal(X, Y, g['sigma'][0,0],\
                        g['sigma'][1,1], g['mu'][0], g['mu'][1]))
        if separate_plots: # only supports 2 clusters currently, TODO
            cmap = pl.cm.get_cmap('jet', 10)    # 10 discrete colors
            ay = pl.subplot(221)
            ay.imshow(Z[0], cmap=cmap, interpolation='bilinear',\
                    origin='lower', extent=ranges)
            az = pl.subplot(222)
            az.imshow(Z[1], cmap=cmap, interpolation='bilinear',\
                    origin='lower', extent=ranges)
        else:
            #ZZ = sum(Z)
            if len(data[0]) < 3:
                for i in range(len(Z)):
                    ax.contour(X, Y, Z[i], 1, colors='k')# colors=colors[i%len(colors)])
    ### /Plot gaussians 

    pl.grid(True)
    pl.show()

    
if __name__ == "__main__":
        #t_data = np.array([[1,1],[11,11]], np.float64)
        #t_data = np.array([[1,1],[0,1],[1,0],[10,10],[11,9],\
        #                [11,12],[9,9],[1,2]], np.float64)
        t_data = np.array([[2,4],[1,2],[1,3],[1,4],[2,1],\
                        [3,1],[4,1],[4,2]], np.float64)
        #t_data = np.array([[1],[3],[1],[2],\
        #                [12],[11],[11],[10]], np.float64)
        t2 = expectation_maximization(t_data, nbiter=1, normalize=False)
        print t2
        plot(t2["clusters"],t_data, "test EM", t2['params'])
        sys.exit(0)

