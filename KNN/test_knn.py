import numpy as np
import knn

def test_simple():
   # print "in tt"
    '''    X=np.array([
        [0,0,0],   
        [1,1,1],   
        ])         
    Y=np.array([ 1, -1 ])
    kNN = knn.kNN(1)
    kNN = kNN.train(X,Y)
    print kNN.apply(X[0]) 
    print kNN.apply(X[1]) 
    print kNN.apply([0,0,1]) 
    print kNN.apply([0,1,1])
    '''
    X=np.array([
        [1,1,1],   
        [2,2,2],   
        ])         
    Y=np.array([ 100, 200 ])
    kNN = knn.kNN(1)
    kNN = kNN.train(X,Y)
    print kNN.apply([2,2,1])

def test_nnclassifier():
    labels=[0,1]
    data=[[0.,0.],[1.,1.]]
    C = knn.kNN(1)
    model = C.train(data,labels)
    print model.apply(data[0])
    print model.apply(data[1])
    print model.apply([.01,.01]) 
    print model.apply([.99,.99]) 
    print model.apply([100,100]) 
    print model.apply([-100,-100]) 
    print model.apply([.9,.9]) 
    middle = model.apply([.5,.5])
    print (middle == 0) or (middle == 1)

def test_approx_nnclassifier():
    import milksets.wine
    features,labels = milksets.wine.load()
    for k in (1,3,5):
        learner = milk.supervised.knn.approximate_knn_learner(k)
        model = learner.train(features[::2], labels[::2])
        testing = model.apply_many(features[1::2])
        print np.mean(testing == labels[1::2]) > .5


test_simple()
