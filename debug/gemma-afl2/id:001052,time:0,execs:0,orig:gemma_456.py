
import cProfile
import time

def my_function(n):
    for _ in range(n):
        a = 1 + 2j

# Use False to check if the function is profiling correctly
if False:
    cProfile.run('my_function(100000)')

# Profile the function without False
cProfile.run('my_function(100000)', profile='my_function.prof')

# Analyze the profile
with open('my_function.prof') as f:
    print(f.read())

# Measure the time taken by the function
start = time.time()
my_function(100000)
end = time.time()

print('Time taken:', end - start)
