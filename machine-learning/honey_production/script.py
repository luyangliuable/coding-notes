import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

#print(df.head())

prod_per_year = df.groupby(['totalprod'])

X = df[['year']].values.reshape(-1, 1)

y = df[['totalprod']].values.reshape(-1, 1)

# plt.scatter(X, y)

#plt.show()
