
# Function to add two numbers with validation using assert statement and docstrings
def add_numbers(num1, num2):
    """
    This function takes two numbers as arguments and returns their sum.
    It also validates that both arguments are numbers.

    Parameters:
    num1 (number): First number to be added.
    num2 (number): Second number to be added.

    Returns:
    The sum of the two given numbers.
    """

    # Documentation for the function's inputs
    assert type(num1) is int or type(num1) is float, "First argument must be a number"
    assert type(num2) is int or type(num2) is float, "Second argument must be a number"

    # Add the two numbers and return the sum
    result = num1 + num2
    return result
