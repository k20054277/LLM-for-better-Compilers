
import numpy as np

# Creating a boolean value 'False'
boolean_value = False
print("Boolean value: ", boolean_value)

# Creating a NumPy array and setting some values to False using mask
arr = np.array([1, 2, 3, 4, 5], dtype=bool)
arr[0] = False
arr[2] = False
print("NumPy array: ", arr)

# Using memoryview for efficient access to contiguous arrays of data
data = np.array([1, 2, 3, 4, 5], dtype=np.float32)
memview = memoryview(data)

# Accessing elements using memoryview is faster than creating a new array copy
print("Element at index 0 using memoryview: ", memview[0])
print("Element at index 0 using numpy array: ", np.array(data)[0])

# Slice memoryview
slice_start = 2
slice_stop = 4
memview_slice = memview[slice_start:slice_stop]
print("Sliced memoryview: ", memview_slice)
print("Sliced numpy array: ", np.array(data)[slice_start:slice_stop])
