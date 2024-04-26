
import assert
import time

# Define a function to find the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Assert that the factorial function works correctly
assert factorial(5) == 120

# Measure the time taken by the factorial function for different numbers
times = []
for i in range(1, 11):
    start_time = time.time()
    factorial(i)
    end_time = time.time()
    times.append(end_time - start_time)

# Print the times taken
print("Times taken by the factorial function:")
print(times)

# Optimize the factorial function by memoization
def factorial(n):
    memoization = {}
    if n == 0:
        return 1
    else:
        if n not in memoization:
            memoization[n] = n * factorial(n-1)
        return memoization[n]

# Assert that the optimized factorial function works correctly
assert factorial(5) == 120

# Measure the time taken by the optimized factorial function for different numbers
times = []
for i in range(1, 11):
    start_time = time.time()
    factorial(i)
    end_time = time.time()
    times.append(end_time - start_time)

# Print the times taken by the optimized factorial function
print("Times taken by the optimized factorial function:")
print(times)