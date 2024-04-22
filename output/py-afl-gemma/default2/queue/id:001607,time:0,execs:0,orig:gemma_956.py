
import pandas as pd
import multiprocessing

# Define a function to be executed in parallel
def square(x):
    return x**2

# Create a list of numbers
nums = [1, 2, 3, 4, 5]

# Create a pool of processes
pool = multiprocessing.Pool(processes=4)

# Map the square function to the list of numbers
results = pool.map(square, nums)

# Print the results
print(results)

# Close the pool
pool.close()
