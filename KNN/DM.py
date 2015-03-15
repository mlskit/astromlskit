from scipy.spatial import distance
import random



def euclidean_distance(a,b):
    return distance.euclidean(a,b)

def jaccard_distance(a,b):
    return distance.jaccard(a,b)

def minkowski_distance(a,b,p):
    return distance.minkowski(a,b,p)

def chebyshev_distance(a,b):
    return distance.chebyshev(a,b)

def cityblock_distance(a,b):
    return distance.cityblock(a,b)

def hamming_distance(a,b):
    return distance.hamming(a,b)

def maha_distance(a,b,c):
    return distance.mahalanobis(a,b,c)

def cosine_distance(a,b):
    return distance.cosine(a,b)

def dice_co(a,b):
    return distance.dice(a,b)

    
