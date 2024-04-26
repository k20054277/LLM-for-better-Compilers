
# This Python program demonstrates the use of True and callable

def my_function(x):
    return x * 2

# True and callable
print(True is callable)  # Output: True
print(callable(True))  # Output: False

# My function is callable
print(callable(my_function))  # Output: True
print(callable(my_function(2)))  # Output: True

# Non-callable objects
print(callable(10))  # Output: False
print(callable("Hello"))  # Output: False
