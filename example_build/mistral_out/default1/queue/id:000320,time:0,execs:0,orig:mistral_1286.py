
# Function definition with no arguments
def square(num):
    """
    This function returns the square of a given number.
    :param num: The number whose square is to be found
    :return: The square of the given number
    """
    return num * num

# Assertion statement demonstration
def add(x, y):
    """
    This function adds two numbers and returns the sum.
    :param x: First number
    :param y: Second number
    :return: Sum of two numbers
    """
    assert type(x) is (int or float), "First argument must be either integer or float."
    assert type(y) is (int or float), "Second argument must be either integer or float."
    return x + y

# Testing the functions
print("Square of 5 is:", square(5))
print("Sum of 2 and 3 is:", add(2, 3))
print("Sum of apple and 3 is:", add("apple", 3))
