
import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Assert
assert factorial(5) == 120

# Performance
start_time = time.time()
factorial(10000)
end_time = time.time()

print("Time taken:", end_time - start_time)
