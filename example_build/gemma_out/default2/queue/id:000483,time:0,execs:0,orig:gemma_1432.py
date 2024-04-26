
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Assert that the array is equal to the expected array
assert np.array_equal(arr, np.array([1, 2, 3, 4, 5]))

# Assert that the array is greater than 0
assert arr > 0

# Assert that the array has a length of 5
assert len(arr) == 5
