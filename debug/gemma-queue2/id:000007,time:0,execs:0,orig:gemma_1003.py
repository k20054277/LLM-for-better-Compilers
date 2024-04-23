
import numpy as np

# Define an array
arr = np.arange(10)

# Check if all elements of the array are greater than 5 and optimize for memory usage
result = np.all(arr > 5) and np.optimize.memory_usage(arr)

# Print the result
print(result)
print(np.optimize.memory_usage(arr))
