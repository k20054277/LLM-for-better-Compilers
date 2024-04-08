
import matplotlib.pyplot as plt
import numpy as np

# Create a NumPy array of 100 random numbers
x = np.random.rand(100)

# Plot the distribution of the numbers using a histogram
plt.hist(x)

# Add a title and labels to the plot
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution of Random Numbers")

# Show the plot
plt.show()

# Check if the plot is False
if not plt.isvalid():
    print("The plot is False")
else:
    print("The plot is True")
