
import numpy as np
import matplotlib.pyplot as plt

# Create some data for the plot
x = np.linspace(0, 10, 100)
y_data1 = np.sin(x)
y_data2 = np.cos(x)

# Define a dictionary with one key having None value and another key having numerical value
my_dict = {'key1': None, 'key2': y_data2}

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the first dataset
ax.plot(x, y_data1, label='sin(x)')

# Demonstrate using None in the dictionary as a placeholder
if my_dict.get('key1'):  # Check if 'key1' has a value before plotting
    ax.plot(x, my_dict['key1'], linestyle='--', label='None Value')

# Label and title for the plot
ax.legend()
ax.set_title('Line Plot using Matplotlib and None')
plt.show()
