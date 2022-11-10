import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()

samples = iris.data

model = KMeans(n_clusters=3)

model.fit(samples)


###############################################################################
#                                   New data                                  #
###############################################################################

# Store the new Iris measurements
new_samples = np.array([[5.7, 4.4, 1.5, 0.4], [6.5, 3. , 5.5, 0.4], [5.8, 2.7, 5.1, 1.9]])
print(new_samples)

# Predict labels for the new_samples
res = print(model.predict(new_samples))
print(res)

###############################################################################
#                                  Visualize                                  #
###############################################################################
# Make a scatter plot of x and y and using labels to define the colors

x = samples[0,:]
y = samples[1,:]

plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')

labels = ['r', 'g', 'b']
plt.scatter(x, y, c=labels, alpha=0.5)
