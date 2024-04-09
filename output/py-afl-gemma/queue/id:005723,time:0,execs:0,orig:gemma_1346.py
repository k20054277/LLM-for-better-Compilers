
def divisible_by_three(n):
    """Yields True if n is divisible by three, False otherwise."""
    yield n % 3 == 0


# Test code
assert divisible_by_three(6) is True
assert divisible_by_three(9) is True
assert divisible_by_three(15) is True
assert divisible_by_three(18) is True
assert divisible_by_three(21) is True

assert divisible_by_three(2) is False
assert divisible_by_three(4) is False
assert divisible_by_three(5) is False
assert divisible_by_three(7) is False
assert divisible_by_three(8) is False
