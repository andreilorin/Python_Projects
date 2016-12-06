from sklearn import tree

clf = tree.DecisionTreeClassifier()

# features [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 38],
     [177, 70, 38], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# labels
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

# train
clf = clf.fit(X, Y)

# assign features
sis = clf.predict([[160, 50, 37]])
bro = clf.predict([[171, 73, 41]])

# predict
print("sis is a", sis)
print("bro is a", bro)

# user features and predict
height = input("your height: ")
weight = input("your weight: ")
shoe_size = input("your shoe size: ")

you = clf.predict([[height, weight, shoe_size]])

print("you are a", you)
