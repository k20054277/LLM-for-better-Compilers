
import numpy as np

# Create an array of 1000 numbers
arr = np.arange(1000)

# Use as to optimize the square of each number
 squares = arr**2

# Print the squares
print(squares)

# Compare the time taken for square using as and without as
import time

start_time = time.time()
squares_without_as = np.square(arr)
end_time = time.time()

start_time2 = time.time()
squares_with_as = arr**2
end_time2 = time.time()

print("Time taken without as:", end_time - start_time)
print("Time taken with as:", end_time2 - start_time2)
