
import numpy as np

# Create a 2D NumPy array of shape (3, 4) filled with zeros
arr = np.zeros((3, 4))
print("Original NumPy Array:")
print(arr)

# Convert NumPy array to memoryview
memview = np.ascontiguousarray(arr).view('f8', order='C')
print("\nMemoryview before modification:")
print(memview)

# Modify memoryview using indexing
memview[0, 1] = 3.14
memview[1, 2] = 2.71
memview[2, 3] = 1.618

# Convert memoryview back to NumPy array
arr_modified = np.ascontiguousarray(memview, dtype=np.float32)
print("\nNumPy Array after modification:")
print(arr_modified)