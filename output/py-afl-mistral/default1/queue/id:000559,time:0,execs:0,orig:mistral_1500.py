
def calculate_square_root(number):
    """
    Calculates the square root of a given number.
    :param number: a non-negative number
    :return: the square root of the number
    """
    assert number >= 0, "Error: The number should be non-negative"
    sqrt = number ** 0.5
    return sqrt

# Test the function with valid and invalid inputs
print(calculate_square_root(9)) # Output: 3.0
print(calculate_square_root(4)) # Output: 2.0

try:
    calculate_square_root(-1)
except AssertionError as error:
    print(error) # Output: Error: The number should be non-negative
