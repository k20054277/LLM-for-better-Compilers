
def add(x, y):
    """Add two numbers"""
    result = x + y
    assert type(x) is (int or float), "First argument should be a number."
    assert type(y) is (int or float), "Second argument should be a number."
    return result

# Test the function with valid inputs
print(add(1, 2)) # Output: 3
print(add(3.5, 2)) # Output: 5.5

# Test the function with invalid inputs
try:
    print(add("a", 1)) # Raise an AssertionError
except AssertionError as error_message:
    print(error_message) # Output: First argument should be a number.

try:
    print(add(1, [2])) # Raise an AssertionError
except AssertionError as error_message:
    print(error_message) # Output: Second argument should be a number.
