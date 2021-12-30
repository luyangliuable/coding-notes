from movies import movie_dafrom movies import movie_dataset, labels
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 5)

classifier.fit(movie_dataset, labels)


movies_to_classify = [[.45, .2, .5], [.25, .8, .9],[.1, .1, .9]]
print(classifier.predict(movies_to_classify))
