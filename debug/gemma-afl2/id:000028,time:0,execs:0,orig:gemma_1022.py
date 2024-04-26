
import numpy as np

# Define an array
arr = np.arange(10)

# Use and to filter elements
res_and = arr[arr % 2 == 0 and arr % 3 == 0]

# Use parallel to filter elements
res_parallel = np.where((arr % 2 == 0) & (arr % 3 == 0))

# Print the results
print("Elements divisible by both 2 and 3:", res_and)
print("Elements divisible by both 2 and 3 (parallel):", res_parallel)
