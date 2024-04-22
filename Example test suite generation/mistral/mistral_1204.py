
# Docstring for the 'square' function
def square(number):
    """
    This function takes one argument, 'number', and returns its square.

    :param number: The number whose square is to be calculated.
    :type number: float or int
    :return: The square of the given number.
    :rtype: float or int
    """
    result = number ** 2
    return result

# Using 'as' keyword to assign the result of a function to a variable with an alias
result = square(3) as squared_number

print("The square of 3 is: ", squared_number)
