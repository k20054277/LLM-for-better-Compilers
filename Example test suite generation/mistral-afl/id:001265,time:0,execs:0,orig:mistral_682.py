
import time
import cProfile

def fibonacci(n):
"""Compute the nth Fibonacci number."""
if n <= 1:
return n
else:
return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
n = 40
start_time = time.time()
result = fibonacci(n)
elapsed_time = time.time() - start_time
print(f"The {n}th Fibonacci number is: {result}")
print(f"Computation took {elapsed_time:.6f} seconds.")

cProfile.run('fibonacci(40)')
