def my_function(x):
    assert x > 0, "x must be positive"
    return x**2

# Test the function with different values of x
print(my_function(1))   # prints 1
print(my_function(-1))  # raises AssertionError: x must be positive