
import numpy as np

# Create a NumPy array
arr = np.arange(10)

# Create a memoryview of the array
arr_view = arr.view(np.dtype('i'))

# Modify the array through the memoryview
arr_view[0] = 20

# Print the modified array
print(arr)

# Output:
# [ 20  1  2  3  4  5  6  7  8  9]
