
# Define a function called is_even
def is_even(n):
    """Returns True if n is even, False otherwise.

    Args:
        n: The number to check.

    Returns:
        True if n is even, False otherwise.
    """

    return n % 2 == 0


# Print the documentation for the is_even function
print(is_even.__doc__)

# Check if 4 is even
print(is_even(4))

# Check if 5 is even
print(is_even(5))
