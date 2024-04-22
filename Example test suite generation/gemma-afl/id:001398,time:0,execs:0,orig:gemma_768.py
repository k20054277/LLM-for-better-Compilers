
import cProfile
import sys

def my_function(n):
    for _ in range(n):
        a = 1 + 2*n

# Profiler to measure the time taken by my_function
cProfile.run('my_function(10000)', 'my_function.prof')

# Open the profiler output in a text editor
with open('my_function.prof') as f:
    print(f.read())

# Analyze the profiler output
print('The lines in the function that took the most time are:')
print(cProfile.run('my_function(10000)').most_time())
