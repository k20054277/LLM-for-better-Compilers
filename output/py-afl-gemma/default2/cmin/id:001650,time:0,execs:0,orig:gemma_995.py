
"""Demonstrates the use of and documentation."""

# Define a function with two parameters
def my_function(a, b):
    """This function takes two parameters, a and b, and returns their product.

    Args:
        a: The first parameter.
        b: The second parameter.

    Returns:
        The product of a and b.
    """

    return a * b


# Print the documentation for my_function
print(my_function.__doc__)

# Print the return value of my_function
print(my_function(2, 3))
