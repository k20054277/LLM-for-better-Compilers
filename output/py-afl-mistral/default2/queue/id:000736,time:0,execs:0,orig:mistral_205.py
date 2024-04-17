
# Boolean values in Python
def is_even(number):
    """
    This function checks if given number is even or not
    :param number: An integer value
    :return: Boolean value - True if number is even, False otherwise
    """
    return number % 2 == 0

# Using False in an if statement
number = 11
if not is_even(number):
    print("Given number is odd")
else:
    print("Given number is even")
