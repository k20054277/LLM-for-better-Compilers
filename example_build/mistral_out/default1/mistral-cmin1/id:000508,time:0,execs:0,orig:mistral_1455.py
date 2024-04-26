
import math

def calc_square_root(number):
    """
    This function calculates the square root of a given number using Python's built-in math.sqrt() function.
    :param number: The input number (must be non-negative)
    :return: The calculated square root of the number
    """

    # Assertion to check if number is non-negative
    assert number >= 0, f"Error: Input number '{number}' must be non-negative."

    # Calculate and return the square root of the number
    result = math.sqrt(number)
    return result

# Test cases
print("Square root of 4 is:", calc_square_root(4))
print("Square root of 9 is:", calc_square_root(9))
print("Square root of -1 is:", calc_square_root(-1))
