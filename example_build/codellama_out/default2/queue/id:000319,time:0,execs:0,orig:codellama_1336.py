def my_function(x):
    assert x > 0, "x must be positive"
    return x + 1

# Example usage
print(my_function(-1)) # Should raise an AssertionError
print(my_function(2)) # Should print