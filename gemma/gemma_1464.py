
def divisible_by_five(n):
    """Checks if a given number is divisible by 5.

    Args:
        n: The number to check.

    Returns:
        True if n is divisible by 5, False otherwise.
    """

    return n % 5 == 0


# Test the divisible_by_five function.

assert divisible_by_five(10) is True
assert divisible_by_five(20) is True
assert divisible_by_five(30) is True
assert divisible_by_five(40) is True
assert divisible_by_five(5) is True

assert divisible_by_five(6) is False
assert divisible_by_five(7) is False
assert divisible_by_five(8) is False
assert divisible_by_five(9) is False
