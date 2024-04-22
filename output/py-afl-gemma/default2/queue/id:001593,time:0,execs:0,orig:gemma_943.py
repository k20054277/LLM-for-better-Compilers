
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [10, 20, 30, 40, 50], "color": ["red", "blue", "green", "orange", "yellow"]})

# Create a scatter plot
plt.scatter(data["x"], data["y"], c=data["color"])

# Add a title and labels
plt.title("Scatter Plot")
plt.xlabel("x")
plt.ylabel("y")

# Show the plot
plt.show()
