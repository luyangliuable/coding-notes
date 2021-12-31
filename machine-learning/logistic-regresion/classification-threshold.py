import numpy as np
from exam import hours_studied, calculated_coefficients, intercept

# Many machine learning algorithms, including Logistic Regression, spit out a classification probability as their result. Once we have this probability, we need to make a decision on what class the sample belongs to. This is where the classification threshold comes in!

# The default threshold for many algorithms is 0.5. If the predicted probability of an observation belonging to the positive class is greater than or equal to the threshold, 0.5, the classification of the sample is the positive class. If the predicted probability of an observation belonging to the positive class is less than the threshold, 0.5, the classification of the sample is the negative class.

# We can choose to change the threshold of classification based on the use-case of our model. For example, if we are creating a Logistic Regression model that classifies whether or not an individual has cancer, we want to be more sensitive to the positive cases, signifying the presence of cancer, than the negative cases.

# In order to ensure that most patients with cancer are identified, we can move the classification threshold down to 0.3 or 0.4, increasing the sensitivity of our model to predicting a positive cancer classification. While this might result in more overall misclassifications, we are now missing fewer of the cases we are trying to detect: actual cancer patients.

def log_odds(features, coefficients, intercept):
  return np.dot(features,coefficients) + intercept

def sigmoid(z):
    denominator = 1 + np.exp(-z)
    return 1/denominator

# Create predict_class() function here
def predict_class(features, coefficients, intercept, threshold):
    calculated_log_odds = log_odds(features, coefficients, intercept)
    probabilities = sigmoid(calculated_log_odds)

    res = []
    for probability in probabilities:
        if probability >= threshold:
            res.append([1])
        else:
            res.append([ 0 ])
    return res


# Make final classifications on Codecademy University data here

final_results = predict_class(hours_studied, calculated_coefficients, intercept, 0.5)
print(final_results)
