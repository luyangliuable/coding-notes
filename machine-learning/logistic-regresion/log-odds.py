import numpy as np
from exam import hours_studied, calculated_coefficients, intercept

# Create your log_odds() function here
def log_odds(features, coefficients, intercept):
    log_odds = np.dot(features, coefficients) + intercept
    return log_odds


# Calculate the log-odds for the Codecademy University data here

calculated_log_odds = log_odds(hours_studied, calculated_coefficients, intercept)
print(calculated_log_odds.reshape(1,-1))
print(hours_studied)
