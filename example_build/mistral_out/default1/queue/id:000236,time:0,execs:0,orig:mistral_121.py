
import numpy as np

# Define a boolean condition using False
condition = False
print("Boolean value 'False': ", bool(False))
print()

# Create a NumPy array of zeros with shape 3x3
zero_array = np.zeros((3, 3), dtype=np.float)
print("Zero NumPy array:")
print(zero_array)
print()

# Create a NumPy array of ones with shape 2x2 using boolean indexing
ones_array = np.ones((2, 2), dtype=np.float)
boolean_condition = np.array([[True, False], [False, True]])
indexed_array = ones_array[boolean_condition]
print("Boolean indexing:")
print(ones_array)
print()
print("Boolean condition:")
print(boolean_condition)
print()
print("Indexed array:")
print(indexed_array)
