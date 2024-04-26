
import numpy as np

# Create a NumPy array
arr = np.arange(10)

# Check if the array is True
print(arr is True)  # Output: False

# Create a memoryview of the array
arr_view = arr.view(np.bool_)

# Check if the memoryview is True
print(arr_view is True)  # Output: True

# Modify the memoryview
arr_view[0] = False

# Check if the original array has changed
print(arr[0])  # Output: 0

# Print the memoryview
print(arr_view)  # Output: [ True False  True  True  True  True  True]
