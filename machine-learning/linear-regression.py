import seaborn
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 12
#intercept:
b = 40

y = []
for i in range(len(months)):
   y.append(m*months[i] + b)

plt.plot(months, revenue, "o")
plt.plot(months, y, "b-")

plt.title("Sandra's Lemonade Stand")

plt.xlabel("Months")
plt.ylabel("Revenue ($)")

plt.show()

# What do you think the revenue in month 13 would be?

