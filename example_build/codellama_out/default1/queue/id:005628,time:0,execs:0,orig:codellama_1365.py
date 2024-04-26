import matplotlib.pyplot as plt

# Define some data to plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and axis object
fig, ax = plt.subplots()

# Use assert to check if the data is valid
assert len(x) == len(y), "Length of x and y arrays must be equal"

# Plot the data using the axis object
ax.plot(x, y)

# Set the title and labels for the axes
ax.set_title("Simple Graph")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

# Show the plot
plt.show()