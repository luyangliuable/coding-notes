class Perceptron:
  def __init__(self, num_inputs=2, weights=[2,1]):
    self.num_inputs = num_inputs
    self.weights = weights

  def weighted_sum(self, inputs):
    # create variable to store weighted sum
    weighted_sum = 0
    for i in range(self.num_inputs):
        weighted_sum += self.weights[i]*inputs[i]

    return weighted_sum

  def activation(self, weighted_sum):
    if weighted_sum >= 0:
        return 1

    return -1

cool_perceptron = Perceptron()

print(cool_perceptron.weighted_sum([24, 55]))
print(cool_perceptron.activation(52))
