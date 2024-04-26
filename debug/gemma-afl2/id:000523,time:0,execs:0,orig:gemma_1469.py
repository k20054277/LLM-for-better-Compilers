
def square(x):
    """Returns the square of a number.

    Args:
        x: The number to square.

    Returns:
        The square of x.
    """

    assert x >= 0
    return x ** 2


# Test code
print(square(5))  # Output: 25
print(square(0))  # Output: 0
print(square(-1))  # Output: Error
