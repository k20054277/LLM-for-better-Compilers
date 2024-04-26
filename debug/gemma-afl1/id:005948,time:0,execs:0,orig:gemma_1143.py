
import numpy as np

# Create a NumPy array
arr = np.arange(10)

# Use as to create a memory view of the array
arr_view = arr.view(np.uint32)

# Print the original array and the memory view
print("Original array:")
print(arr)

print("Memory view:")
print(arr_view)

# Modify the memory view
arr_view[0] = 100

# Print the modified array
print("Modified array:")
print(arr)
