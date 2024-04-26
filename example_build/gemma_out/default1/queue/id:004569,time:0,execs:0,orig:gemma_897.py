
import numpy as np

# Create a NumPy array
arr = np.arange(10)

# Create a memoryview of the array
arr_view = arr.view(np.uint32)

# Modify the array through the memoryview
arr_view[0] = 100

# Print the modified array
print(arr)
