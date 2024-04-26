
def factorial(n):
    """Calculates the factorial of a number using recursion.

    The factorial of a number is the product of all the positive integers less than or equal to that number.

    For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

    Args:
        n: The number to calculate the factorial of.

    Returns:
        The factorial of n.
    """

    # If n is 0, return 1.
    if n == 0:
        return 1

    # Otherwise, return n multiplied by the factorial of n-1.
    else:
        return n * factorial(n-1)


# Print the factorial of 5.
print(factorial(5))
