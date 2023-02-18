from tree import training_data, training_labels, testing_data, testing_labels, make_random_forest, make_single_tree, classify
import numpy as np
import random
from collections import Counter

# Seed the random number generators for reproducibility.
np.random.seed(1)
random.seed(1)

# Build a single decision tree and a random forest using the training data.
tree = make_single_tree(training_data, training_labels)
forest = make_random_forest(40, training_data, training_labels)

# Initialize counters to keep track of the number of correct predictions.
single_tree_correct = 0
forest_correct = 0

# Classify the testing data using the single tree and the random forest, and update the counters.
for i in range(len(testing_data)):
  prediction = classify(testing_data[i], tree)
  if prediction == testing_labels[i]:
    single_tree_correct += 1
    
  predictions = []
  for forest_tree in forest:
    predictions.append(classify(testing_data[i], forest_tree))
  forest_prediction = max(predictions,key=predictions.count)
  if forest_prediction == testing_labels[i]:
    forest_correct += 1
    
# Print the accuracy of the single tree and the random forest.
print(single_tree_correct/len(testing_data))
print(forest_correct/len(testing_data))
