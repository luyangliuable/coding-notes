import codecademylib3_seaborn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from exam import exam_features_scaled, passed_exam_2

# Train a sklearn logistic regression model on the normalized exam data
model_2 = LogisticRegression()
model_2.fit(exam_features_scaled,passed_exam_2)

# Assign and update coefficients

coefficients = model_2.coef_


# Plot bar graph

coefficients = coefficients.tolist()[0]

print(exam_features_scaled)
x = exam_features_scaled.tolist()[0]

print(x)

plt.bar(x, coefficients, edgecolor ='k')

plt.show()
