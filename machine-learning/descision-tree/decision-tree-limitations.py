from cars import training_points, training_labels, testing_points, testing_labels   # Importing the training and testing data from the cars module
from sklearn.tree import DecisionTreeClassifier    # Importing the DecisionTreeClassifier class from the sklearn.tree module

classifier = DecisionTreeClassifier(random_state=0, max_depth=11)   # Instantiating a DecisionTreeClassifier object with a max depth of 11 and a random state of 0
classifier.fit(training_points, training_labels)    # Fitting the classifier to the training data
print(classifier.score(testing_points, testing_labels))   # Printing the accuracy of the classifier on the testing data
