from sklearn import tree

x = [[150, 1], [160, 1], [130,0],[120, 0]]
y = [5,5,10,10]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

print_(clf.predict([145,0]))