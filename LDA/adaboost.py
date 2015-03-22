import math
import numpy
import operator

from abstract_classifier import Classifier

class AdaBoost(Classifier):
    def __init__(self, weak_classifier_type):
        Classifier.__init__(self)
        self.WeakClassifierType = weak_classifier_type

    def train(self, T):
        X = self.X
        Y = self.Y
        d,N = X.shape
        w = (1.0/N)*numpy.ones(N)
        self.weak_classifier_ensemble = []
        self.alpha = []
        for t in range(T):
            weak_learner = self.WeakClassifierType()
            weak_learner.set_training_sample(X,Y)
            weak_learner.weights = w
            weak_learner.train()
            Y_pred = weak_learner.predict(X)
            e = (sum(0.5*w*abs((Y-Y_pred)))/sum(w))
            alpha = 0.5*math.log((1-e)/e)
            w *= numpy.exp(-alpha*Y*Y_pred)
            w /= sum(w)
            self.weak_classifier_ensemble.append(weak_learner)
            self.alpha.append(alpha)
        self.T = T

    def predict(self,X):
        d,N = X.shape
        Y = numpy.zeros(N)
        for t in range(self.T):
            weak_learner = self.weak_classifier_ensemble[t]
            Y += self.alpha[t]*weak_learner.predict(X)
        return Y

    def test_on_training_set(self, X, Y, T, threshold=0):
        self.set_training_sample(X,Y)
        self.train(T)
        o = self.predict(X)
        o[numpy.where(o>threshold)[0]] = 1
        o[numpy.where(o<threshold)[0]] = -1
        oY = o*Y
        accuracy = (sum(oY)+len(Y))/(2*len(Y))
        return accuracy, o, Y
