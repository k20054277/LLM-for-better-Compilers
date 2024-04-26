
# Define a function
def my_function(x):
    # Return None if x is None
    if x is None:
        return None

    # Otherwise, return x squared
    else:
        return x ** 2

# Test the function
print(my_function(None))  # Output: None
print(my_function(5))  # Output: 25
