
import numpy as np
import matplotlib.pyplot as plt

# Define some data
x = np.linspace(-10, 10, 400)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create figures and subplots
fig, axs = plt.subplots(ncols=2, figsize=(12, 6))

# Plot sine function
axs[0].plot(x, y_sin, label='Sine')
axs[0].set_title('Sine Function')
axs[0].legend()
axs[0].grid()

# Plot cosine function
axs[1].plot(x, y_cos, label='Cosine')
axs[1].set_title('Cosine Function')
axs[1].legend()
axs[1].grid()

# Show the figures
plt.show()
