def my_function(x):
    return x > 0

print(my_function(5))  # Output: True
print(my_function(-5))  # Output: False

print(callable(my_function))  # Output: True
print(callable(False))  # Output: False