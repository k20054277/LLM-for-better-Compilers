
import time
import assert

# Define a function to measure the time taken by a loop
def measure_time(n):
    start_time = time.time()
    for _ in range(n):
        pass
    end_time = time.time()
    return end_time - start_time

# Assert that the time taken is less than 1 second
assert measure_time(1000) < 1

# Profile the function to identify the bottlenecks
import cProfile
cProfile.run('measure_time(1000)')

# Print the profile report
print(cProfile.run('measure_time(1000)'))
