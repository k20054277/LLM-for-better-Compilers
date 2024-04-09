
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Check if all elements of the array are greater than 3
print(np.all(arr > 3))  # Output: False

# Check if any element of the array is less than 2
print(np.any(arr < 2))  # Output: True

# Print the maximum value of the array
print(np.max(arr))  # Output: 5

# Print the minimum value of the array
print(np.min(arr))  # Output: 1

# Print the average value of the array
print(np.mean(arr))  # Output: 3.0
