import matplotlib.pyplot as plt

# Create some sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Use and to create a mask for the data that meets both conditions
mask = (x > 2) & (y < 6)

# Create a plot of the data
plt.plot(x[mask], y[mask])
plt.show()