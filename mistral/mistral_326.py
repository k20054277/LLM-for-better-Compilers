
import numpy as np

# Create a NumPy array
array_numpy = np.arange(15).reshape((3, 5))
print("NumPy Array:")
print(array_numpy)

# Assign None to a variable
none_variable = None

# Use memoryview to access a part of NumPy array as read-only memory view
memoryview_array = memoryview(array_numpy[1:2, 3:])
print("\nMemory View:")
print(memoryview_array)
print(f"Shape: {memoryview_array.shape}")
print(f"Data Type: {memoryview_array.dtype}")
print(f"Size: {memoryview_array.size}")

# Attempt to modify memory view, which should raise an error
try:
    memoryview_array[0, 0] = 99
except Exception as e:
    print("\nError:")
    print(e)

# Accessing the None variable will result in a 'NameError: name "none_variable" is not defined' error if not assigned a value beforehand.
