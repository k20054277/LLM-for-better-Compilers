
import time

# Define a function to demonstrate False and optimization
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Optimize the factorial function by memoization
def memoized_factorial(n):
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = factorial(n)
        return cache[n]
    return inner(n)

# Benchmark the two functions
start_time = time.time()
for i in range(1, 11):
    factorial(i)
end_time = time.time()
print("Time taken by factorial function:", end_time - start_time)

start_time = time.time()
for i in range(1, 11):
    memoized_factorial(i)
end_time = time.time()
print("Time taken by memoized factorial function:", end_time - start_time)
