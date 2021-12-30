import con
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

line_fitter = LinearRegression()


temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]


line_fitter.fit(temperature, sales)

sales_predict = [line_fitter.predict(temp) for temp in temperature]
sales_predict = sales_predict.reshape(-1, 1)

plt.plot(temperature, sales, 'o')
plt.show()

