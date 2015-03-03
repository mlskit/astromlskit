from NaiveBayes import *
c=Classy()
c.train([1,2,3],"a")
c.train([3,4,5],"b")
c.train([1,1,1],"a")
print c.classify([1,2,3])
