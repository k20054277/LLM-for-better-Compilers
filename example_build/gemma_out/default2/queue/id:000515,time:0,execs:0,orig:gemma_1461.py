
def factorial(n):
    """Calculates the factorial of a number.

    The factorial of a number is the product of all the positive integers less than or equal to that number.

    For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

    Args:
        n: The number to calculate the factorial of.

    Returns:
        The factorial of n.
    """

    # Base case: Factorial of 0 is 1.
    if n == 0:
        return 1

    # Recursive case: Factorial of n is n multiplied by factorial of n-1.
    else:
        return n * factorial(n-1)

# Test code:
assert factorial(0) == 1
assert factorial(5) == 120
assert factorial(6) == 720
