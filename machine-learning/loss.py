x = [1, 2, 3x = [1,x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0


y_predicted1 = [x_val*m1 + b1 for x_val in x]

total_loss1 = 0
for i, enum_y_predicted1 in enumerate(y_predicted1):
    total_loss1 += (( y[i] - enum_y_predicted1 )**2)


#y = 0.5x + 1
m2 = 0.5
b2 = 1


y_predicted2 = []
for i, enum_x in enumerate(x):
    y_predicted2.append(m2*enum_x + b2)


total_losses2 = [(y[i] - y_predicted2[i])**2 for i in range(len(y))]
total_loss2 = 0
for val in total_losses2:
  total_loss2 += val

print(total_loss2)
print(total_loss1)

better_fit = 2
