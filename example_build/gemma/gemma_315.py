
# False and Callable

def my_callable(x):
    return x * 2

# False

print(False)  # Output: False

# Callable

print(callable(False))  # Output: False

# True and Callable

print(True)  # Output: True

print(callable(True))  # Output: True

# My callable

print(callable(my_callable(5)))  # Output: True

print(my_callable(5))  # Output: 10
