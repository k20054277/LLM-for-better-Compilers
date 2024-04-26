
import math

def check_number(n, min_value, max_value):
    """
    This function checks if a given number 'n' is within the specified range of minimum value 'min_value' and maximum value 'max_value'.
    :param n: The number to be checked.
    :param min_value: The minimum allowed value.
    :param max_value: The maximum allowed value.
    """

    # Checking if the number is within the specified range using assert statement
    assert min_value <= n <= max_value, f"Number {n} is not within the range ({min_value}, {max_value})"

    # Alternatively, you can also use math library functions to check the conditions:

    # Check if the number is positive
    if n < 0:
        print("The given number must be non-negative.")
        raise ValueError("Negative number detected.")

    # Calculate the square root of a number using math.sqrt() function
    sqrt_n = math.sqrt(abs(n))

    print(f"Square root of {n} is approximately: {sqrt_n}")

# Testing the function with valid input
check_number(9, 1, 10)

# Testing the function with invalid input
try:
    check_number(-5, 1, 10)
except AssertionError as e:
    print(e)

# Testing the function with floating-point number as input
check_number(2.5, 1, 3)
