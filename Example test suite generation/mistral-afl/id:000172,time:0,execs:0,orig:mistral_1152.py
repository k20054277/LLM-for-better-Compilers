
import numpy as np
import matplotlib.pyplot as plt

# Load data from a text file using NumPy's genfromtxt() function
data = np.genfromtxt('data.csv', delimiter=',')

# Use the context manager with the np.split() function to split the data into columns
x, y = np.split(data, 2, axis=1)

# Plot the data using Matplotlib
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter plot of X and Y')

plt.show()
