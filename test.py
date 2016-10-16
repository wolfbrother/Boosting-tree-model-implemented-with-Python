data = {'x':np.array([1,2,3,4,5,6,7,8,9,10]),
        'y':np.array([5.56,5.70,5.91,6.40,6.80,7.05,8.90,8.70,9.00,9.05])}
boostingtree = BoostingTree(data)
predictlist = boostingtree.predict(np.array([1,2,3,4,5,6,7,8,9,10]))
valuelist = np.array([5.56,5.70,5.91,6.40,6.80,7.05,8.90,8.70,9.00,9.05])
loss = np.sum(np.power(predictlist - valuelist,2))
print '平方误差：',str(loss) 
