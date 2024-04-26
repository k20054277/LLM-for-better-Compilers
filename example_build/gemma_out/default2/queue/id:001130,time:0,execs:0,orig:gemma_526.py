
import conda
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, None, 4, 5])

# Print the array
print(arr)

# Check if the array contains None
print(None in arr)

# Remove None from the array
arr_no_none = np.where(arr is not None, arr, None)

# Print the array without None
print(arr_no_none)
