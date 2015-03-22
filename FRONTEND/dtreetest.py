from dtree import Tree, Data

tree = Tree.build(Data('cdata21.txt'))
result = t.test(Data('regression-testing.csv'))
#prediction = tree.predict(dict(a=2,b=3,c=1,d=2))
print 'best:',prediction.best
print 'probs:',prediction.probs

##tree = Tree.build(Data('regression-training.csv'))
##result = t.test(Data('regression-testing.csv'))
##print 'MAE:',result.mean
##prediction = tree.predict(dict(feature1=123, feature2='abc', feature3='hot'))
##print 'mean:',prediction.mean
##print 'variance:',prediction.variance
