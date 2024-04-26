
def divisible_by_five(n):
    """Checks if a number is divisible by 5.

    Args:
        n: The number to check.

    Returns:
        True if n is divisible by 5, False otherwise.
    """

    return n % 5 == 0


# Test code
assert divisible_by_five(10) is True
assert divisible_by_five(25) is True
assert divisible_by_five(30) is True
assert divisible_by_five(35) is True

assert divisible_by_five(6) is False
assert divisible_by_five(11) is False
assert divisible_by_five(16) is False

print("All tests passed!")
