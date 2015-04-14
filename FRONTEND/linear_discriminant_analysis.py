import math
import operator
import numpy as np
import scipy as sp
import scipy.linalg as linalg

class LDA():
    """
    Classification using linear discriminant analysis (LDA)
    References:
      [1]Duda et al., Pattern Classification, 2nd edition.
      [2]http://www.public.asu.edu/~jye02/CLASSES/Fall-2007/NOTES/LDA.pdf
    Example:
        from numpy import loadtxt
        X = loadtxt('iris_X.txt',delimiter=',')
        Y = loadtxt('iris_Y.txt',delimiter=',')
        X_train = X[::2]
        Y_train = Y[::2]
        X_test = X[1::2]
        Y_test = Y[1::2]
        from lda import LDA_Classifier
        c = LDA_Classifier()
        c.Train(X_train,Y_train)
        Y_raw = c.Test(X_test)
        label = Y_raw.argmin(axis=1)
        # check the classification accuracy
        label + 1 - Y_test
    """
    def train(self,X,Y):
        """Train a LDA classifier from a labeled dataset."""
        classLabels = np.unique(Y)
        classNum = len(classLabels)
        datanum,dim = X.shape
        totalMean = np.mean(X,0)

        partition = [np.where(Y==label)[0] for label in classLabels]
        classMean = [(np.mean(X[idx],0),len(idx)) for idx in partition]

        #compute the within-class scatter matrix
        W = np.zeros((dim,dim))
        for idx in partition:
            W += np.cov(X[idx],rowvar=0)*len(idx)
        #compute the between-class scatter matrix
        B = np.zeros((dim,dim))
        for mu,class_size in classMean:
            offset = mu - totalMean
            B += np.outer(offset,offset)*class_size

        #solve the generalized eigenvalue problem for discriminant directions
        ew, ev = linalg.eig(B,W+B)
        sorted_pairs = sorted(enumerate(ew), key=operator.itemgetter(1), reverse=True)
        selected_ind = [ind for ind,val in sorted_pairs[:classNum-1]]
        self.discriminant_vector = ev[:,selected_ind]
        # project the mean vectors of each class onto the LDA space
        self.projected_centroid = [np.dot(mu,self.discriminant_vector) for mu,class_size in classMean]

    def predict(self,X):
        """Apply the trained LDA classifier on test data."""
        #project test data onto LDA directions
        projected_data  = np.dot(X,self.discriminant_vector)
        projected_centroid = self.projected_centroid
        dist = [linalg.norm(data-centroid) for data in projected_data for centroid in projected_centroid]
        Y_raw = np.reshape(np.array(dist), (len(X),len(projected_centroid)))
        return Y_raw
        #then use "label = Y_raw.argmin(axis=1)" to obtain the class labels
