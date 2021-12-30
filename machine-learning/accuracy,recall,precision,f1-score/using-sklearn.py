from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]


accuracy = accuracy_score(labels, guesses)
precision = precision_score(labels, guesses)
recall = recall_score(labels, guesses)
f_1 = f1_score(labels, guesses)


print(accuracy)
print(precision)
print(recall)
print(f_1)
