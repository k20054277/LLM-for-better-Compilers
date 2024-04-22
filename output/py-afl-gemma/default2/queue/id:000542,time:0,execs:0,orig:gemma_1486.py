
"""Demonstrate the use of assert and documentation."""


def factorial(n):
    """Calculates the factorial of a number.

    Args:
        n: The number to calculate the factorial of.

    Returns:
        The factorial of n.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Test the factorial function.
assert factorial(5) == 120
assert factorial(0) == 1

# Document the function.
print(factorial.__doc__)
