#K nearest Neighbour classification using python
#using numpy and scipy
#uses sample data set of cancer obtained from google 
# initial K values are loaded from sample set as 1 3 7 11

import numpy as np
import scipy.spatial.distance as ssd
import time
 
def read_data(fn):
    """ read dataset and separate into input data
        and label data
    """
 
    # read dataset file
    with open(fn) as f:
        raw_data = np.loadtxt(f, delimiter= ',', dtype="float", 
            skiprows=1, usecols=None)
    # initilize list
    data = []; label = []
    #assign input data and label data
    for row in raw_data:
        data.append(row[:-1])
        label.append(int(row[-1]))
    # return input data and label data
    return np.array(data), np.array(label)
 
def knn(k, dtrain, dtest, dtr_label, dist=1):
    """ k-nearest neighbors """
 
    # initialize list to store predicted class
    pred_class = []
    # for each instance in data testing,
    # calculate distance in respect to data training
    for ii, di in enumerate(dtest):
        distances = []  # initialize list to store distance
        for ij, dj in enumerate(dtrain):
            # calculate distances
            distances.append((calc_dist(di,dj,dist), ij))
        # k-neighbors
        k_nn = sorted(distances)[:k]
        # predict the class for the instance
        pred_class.append(classify(k_nn, dtr_label))
 
    # return prediction class
    return pred_class
 
def calc_dist(di,dj,i=1):
    """ Distance calculation for every
        distance functions in use"""
    if i == 1:
        return ssd.euclidean(di,dj) # built-in Euclidean fn
    elif i == 2:
        return ssd.cityblock(di,dj) # built-in Manhattan fn
    elif i == 3:
        return ssd.cosine(di,dj)    # built-in Cosine fn
 
def classify(k_nn, dtr_label):
    """ Classify instance data test into class"""
 
    dlabel = []
    for dist, idx in k_nn:
        # retrieve label class and store into dlabel
        dlabel.append(dtr_label[idx])
 
    # return prediction class
    return np.argmax(np.bincount(dlabel))
 
def evaluate(result):
    """ Evaluate the prediction class"""
 
    # create eval result array to store evaluation result
    eval_result = np.zeros(2,int)
    for x in result:
        # increment the correct prediction by 1
        if x == 0:
            eval_result[0] += 1
        # increment the wrong prediction by 1
        else:
            eval_result[1] += 1
    # return evaluation result
    return eval_result
 
