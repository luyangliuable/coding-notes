import seaborn
import numpy as np
import matplotlib.pyplot as plt

# Create your sigmoid function here
def sigmoid(z):
    denominator =  1 + np.exp(-z)
    return 1/denominator

# Calculate the sigmoid of the log-odds here

calculated_log_odds = [-1.76125712, -1.55447221, -1.3476873,  -1.14090239, -0.93411748, -0.72733257, -0.52054766, -0.31376275, -0.10697784,  0.09980707,  0.30659198,  0.51337689, 0.7201618,   0.92694671,  1.13373162,  1.34051653,  1.54730144,  1.75408635, 1.96087126,  2.16765617]

probabilities = []
for item in calculated_log_odds:
    probabilities.append(sigmoid( item ))

print(calculated_log_odds)
print(probabilities)
plt.plot(calculated_log_odds, probabilities, 'r-')
plt.legend([ 'log-odds', 'probabilities' ])
plt.savefig('sigmond-function.jpg')
plt.close()
