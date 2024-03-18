
"""Demonstrating True and Documentation"""

# Define a function to check if a number is even
def is_even(num):
    """Checks whether a number is even.

    Args:
        num: The number to check.

    Returns:
        True if num is even, False otherwise.
    """

    return num % 2 == 0


# Print True or False based on the result of is_even(5)
print(is_even(5))  # Output: False

# Print the documentation for is_even()
print(is_even.__doc__)  # Output:
# Demonstrating True and Documentation

# Define a function to check if a number is even.

# Args:
#   num: The number to check.

# Returns:
#   True if num is even, False otherwise.
