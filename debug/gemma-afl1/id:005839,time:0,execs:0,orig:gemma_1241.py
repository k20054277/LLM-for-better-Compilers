
"""Demonstrating the use of as and documentation"""


def square(x):
    """Returns the square of a number.

    Args:
        x: The number to square.

    Returns:
        The square of x.
    """

    return x ** 2


print(square(5))  # Output: 25

print(square.__doc__)  # Output: Demonstrating the use of as and documentation

print(square.__name__)  # Output: square
