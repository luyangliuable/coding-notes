import numpy as np

p_rain_and_gym = .3*3/5

p_disease_and_correct = (1 - 0.01) * (1.0 / 100000)

print(p_disease_and_correct)

# P(test incorrect) = 0.01
# P(no disease) = 1 - (1.0 / 100000)
p_no_disease_and_incorrect = 0.01 * (1 - (1.0 / 100000))

print(p_no_disease_and_incorrect)
