
from hierarchical import HierarchicalClustering
from difflib import SequenceMatcher
import unittest

data = [12,34,23,32,46,96,13]
cl = HierarchicalClustering(data, lambda x,y: abs(x-y))


temp=len(cl.getlevel(0))

for i in range(0,100):
    print cl.getlevel(i)
    if len(cl.getlevel(i))<temp:
        temp=len(cl.getlevel(i))
