
# This Python program demonstrates the use of assert and /= operators.

def divide(x, y):
    assert y != 0  # Assert that y is not equal to 0
    return x / y

# Test code
divide(10, 2)  # Output: 5
divide(10, 0)  # Expected error: ZeroDivisionError

# The following line should raise a ZeroDivisionError
# divide(10, 0)  # Error: ZeroDivisionError
