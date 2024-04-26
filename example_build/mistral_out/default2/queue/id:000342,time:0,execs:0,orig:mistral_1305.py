
import math

def square_root(number):
    """Calculate the square root of a number. Raise an error if the number is negative."""

    assert number >= 0, "Error: The number must be greater than or equal to zero."

    result = math.sqrt(number)

    return result

# Test cases
print(square_root(4))
print(square_root(16))
print(square_root(-1))
