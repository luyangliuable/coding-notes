# import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# From sklearn.cluster, import KMeans class

iris = datasets.load_iris()

samples = iris.data

# Use KMeans() to create a model that finds 3 clusters
model = KMeans(n_clusters=3);

# Use .fit() to fit the model to samples
print(iris)
model.fit(iris[:,0],iris[:,1])

# Use .predict() to detemine the labels of samples
labels = model.predict(samples[:0]);

# Print the labels
print(labels)

