from matplotlib import pyplot as plt

x_values = [1, 2, 3, 4]
y_values = [5, 4, 7, 8]

plt.scatter(x_values, y_values)

other_x_values = [1, 2, 3, 4]
otherx_y_values = [4, 2, 3, 9]

plt.plot(other_x_values, otherx_y_values, color="red")

plt.title("Sample Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()