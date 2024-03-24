# Demonstrate the use of True and False in Python

# Print a message if the value is true
if True:
    print("Value is true")

# Print a message if the value is false
if False:
    print("Value is false")

# Use profiling to measure the performance of a function
import cProfile

def my_function(n):
    total = 0
    for i in range(n):
        total += i**2
    return total

cProfile.run('my_function(10)')