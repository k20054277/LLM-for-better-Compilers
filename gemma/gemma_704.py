
import numpy as np

# Define a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Check if the array is True
print(arr is True)  # Output: False

# Check if the array is numeric
print(np.issnumeric(arr))  # Output: True

# Print the array
print(arr)  # Output: [1 2 3 4 5]

# Perform operations on the array
print(arr ** 2)  # Output: [1 4 9 16 25]

# Create a boolean mask
mask = arr % 2 == 0

# Print the elements of the array that satisfy the mask
print(arr[mask])  # Output: [2 4]
