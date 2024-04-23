
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Use the and operator to check if each element in the array is greater than 2 and less than 5
print(np.and_(arr > 2, arr < 5))

# Output:
# [ True  True  True  True False]
