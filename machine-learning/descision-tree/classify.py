# Import necessary functions and data from the `tree` module
from tree import build_tree, print_tree, car_data, car_labels, classify
import random

# Set a random seed for reproducibility
random.seed(4)

# Define the features of the unlabeled point
unlabeled_point = ['high', 'vhigh', '3', 'more', 'med', 'med']

# Initialize an empty list to hold the predictions
predictions = []

# Build 20 decision trees using random subsets of the car data and labels
for i in range(20):
    # Randomly select 1000 indices from the car data
    indices = [random.randint(0, 999) for i in range(1000)]
    # Use the selected indices to get the corresponding subsets of data and labels
    data_subset = [car_data[index] for index in indices]
    labels_subset = [car_labels[index] for index in indices]
    # Build a decision tree using the subset data and labels
    subset_tree = build_tree(data_subset, labels_subset)
    # Make a prediction on the unlabeled point using the subset tree, and append the prediction to the list of predictions
    predictions.append(classify(unlabeled_point, subset_tree))

# Choose the prediction that occurs most frequently in the list of predictions
final_prediction = max(predictions, key=predictions.count)
