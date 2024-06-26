import matplotlib.pyplot as plt

# Create a figure object
fig = plt.figure()

# Create a subplot
ax = fig.add_subplot(1, 1, 1)

# Set the x and y data for the plot
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

# Plot the data
ax.plot(x, y)

# Show the plot
plt.show()