import numpy as np

# Create a numpy array
a = np.array([1, 2, 3, 4])

# Convert the array to a memory view using as
mv = a.as_memoryview()

# Print the contents of the memory view
print(mv)

# Modify the contents of the memory view
mv[0] = 5

# Check that the changes have been propagated to the original array
print(a)