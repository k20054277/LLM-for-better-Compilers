
import math
import timeit

# Function 1: Recursive implementation
def factorial_recursive(n):
"""Recursively calculates the factorial of a given number."""
if n == 0:
return 1
else:
return n * factorial_recursive(n - 1)

# Function 2: Iterative implementation
def factorial_iterative(n):
"""Iteratively calculates the factorial of a given number."""
result = 1
for i in range(1, n + 1):
result *= i
return result

# Profiling using timeit module
if __name__ == "__main__":
# Recursive implementation
num_recursive = 5
print(f"Recursive Factorial ({num_recursive}):")
rec_time = timeit.timeit(lambda: factorial_recursive(num_recursive), number=100)
print(f"Time taken: {rec_time} seconds")
result_as_recursive = factorial_recursive(num_recursive)
print(f"Result: {result_as_recursive}")

# Iterative implementation
num_iterative = 5
print(f"\nIterative Factorial ({num_iterative}):")
itv_time = timeit.timeit(lambda: factorial_iterative(num_iterative), number=100)
print(f"Time taken: {itv_time} seconds")
result_as_iterative = factorial_iterative(num_iterative)
print(f"Result: {result_as_iterative}")
