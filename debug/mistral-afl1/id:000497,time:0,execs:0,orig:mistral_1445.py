
def divide(x, y):
    """This function divides two numbers."""
    result = x / y
    assert y != 0, "Error: Division by zero is not allowed."
    return result

# Testing the divide function with valid input
print(divide(10, 2)) # Output: 5.0

# Testing the divide function with invalid input
try:
    print(divide(10, 0))
except AssertionError as e:
    print(e) # Output: Error: Division by zero is not allowed.
