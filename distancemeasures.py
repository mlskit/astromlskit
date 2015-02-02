from scipy.spatial import distance
import random



def euclidean_distance(a,b):
    print distance.euclidean(a,b)

def jaccard_distance(a,b):
    print distance.jaccard(a,b)

def minkowski_distance(a,b,p):
    print distance.minkowski(a,b,p)

def chebyshev_distance(a,b):
    print distance.chebyshev(a,b)

def cityblock_distance(a,b):
    print distance.cityblock(a,b)

def hamming_distance(a,b):
    print distance.hamming(a,b)

def maha_distance(a,b,c):
    print distance.mahalanobis(a,b,c)

def cosine_distance(a,b):
    print distance.cosine(a,b)

def dice_co(a,b):
    print distance.dice(a,b)

    
