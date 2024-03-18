import numpy as np

# Create two arrays with different shapes and data types
arr1 = np.array([True, False, True])
arr2 = np.array([False, True, False])

# Use the and operator to perform element-wise logical AND on the arrays
result = arr1 and arr2

print(result)