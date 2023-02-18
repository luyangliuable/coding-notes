from tree import build_tree, print_tree, car_data, car_labels
import random
random.seed(4)

# tree = build_tree(car_data, car_labels)
# print_tree(tree)

indices = [random.randint(0, 999) for i in range(1000)]
print(len(indices))
print(len(car_data))

data_subset = [car_data[i] for i in indices]
labels_subset = [car_labels[i] for i in indices]

subset_tree = build_tree(data_subset, labels_subset)
print_tree(subset_tree)
