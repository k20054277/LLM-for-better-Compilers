
import matplotlib.pyplot as plt

# Define some sample data
x = [i for i in range(10)]
y = [i**2 for i in range(10)]

# Create a scatter plot
plt.scatter(x, y)

# Add a title and labels
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Scatter Plot")

# Show the plot
plt.show()
