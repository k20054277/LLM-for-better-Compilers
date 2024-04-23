
import numpy as np
import matplotlib.pyplot as plt

def calculate_mean(data):
    """Calculate the mean of given data."""
    assert isinstance(data, np.ndarray), "Input should be a NumPy array."
    return np.mean(data)

# Generate some random data for demonstration
data = np.random.rand(5)

# Calculate mean and check if it's within expected range (0-1 in this case) using assert statement
mean = calculate_mean(data)
assert 0 <= mean <= 1, f"Mean of data should be between 0 and 1. Got: {mean}"

# Visualize the data using matplotlib
plt.hist(data, bins=np.linspace(0, 1, 20), density=True)
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Data Distribution')
plt.show()
