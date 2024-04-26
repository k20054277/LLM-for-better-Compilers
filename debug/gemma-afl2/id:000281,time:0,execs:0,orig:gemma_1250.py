
import time

# Define a function to measure the time taken by the as keyword
def measure_as(func):
    start = time.time()
    a = func()
    end = time.time()
    return end - start

# Define a function that takes a long time to execute
def long_function():
    # Some code that takes a long time to execute
    for i in range(100000):
        pass

# Measure the time taken by the as keyword
time_taken = measure_as(long_function)

# Print the time taken
print("Time taken by as:", time_taken)

# Measure the time taken by a traditional function call
time_taken_traditional = measure_time(long_function)

# Print the time taken by a traditional function call
print("Time taken by traditional function call:", time_taken_traditional)
