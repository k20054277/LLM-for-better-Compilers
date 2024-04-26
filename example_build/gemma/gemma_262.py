
import numpy as np
import matplotlib.pyplot as plt

# Create a sample data set
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)

# Add a label to the x-axis
plt.xlabel("Time")

# Add a label to the y-axis
plt.ylabel("Amplitude")

# Add a title to the plot
plt.title("Sinusoidal Function")

# Show the plot
plt.show()
