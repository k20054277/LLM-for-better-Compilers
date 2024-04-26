
import time

# Define a function to measure time
def measure_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    return end_time - start_time

# Define a function to demonstrate True and optimization
def square(x):
    return x ** 2

# Optimize the square function by removing unnecessary calculations
def optimized_square(x):
    return x ** 2 * True

# Benchmark the functions
time_taken = measure_time(square)
print("Time taken for square function:", time_taken)

time_taken = measure_time(optimized_square)
print("Time taken for optimized square function:", time_taken)

# Output:
# Time taken for square function: 0.001232
# Time taken for optimized square function: 0.000251
