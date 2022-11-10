import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()

samples = iris.data

model = KMeans(n_clusters=3)

# Code Start here:
num_clusters = [i for i in range(1, 9)]
inertias = []

for i in range(len(num_clusters)):
    inertias[i] = model.fit(samples[0,3], [1,3])

plt.plot(num_clusters, inertias, '-o')

plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')

plt.show()
