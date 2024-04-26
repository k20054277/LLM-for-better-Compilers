
# This Python program demonstrates the use of assert and <

def check_even(num):
    """Checks if a number is even.

    Args:
        num: The number to check.

    Returns:
        True if num is even, False otherwise.
    """

    return num % 2 == 0


# Asserting that check_even returns True for even numbers
assert check_even(0)
assert check_even(2)
assert check_even(4)

# Asserting that check_even returns False for odd numbers
assert not check_even(1)
assert not check_even(3)
assert not check_even(5)

# Trying to assert an impossible condition
assert check_even(-1)  # This will raise an error
