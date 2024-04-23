
import matplotlib.pyplot as plt
import numpy as np

# Define some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sine Function')
plt.show()

# Print True or False
print(True)
print(False)
