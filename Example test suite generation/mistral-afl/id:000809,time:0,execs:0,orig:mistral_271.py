
# Importing the math module for demonstration purposes
import math

def my_function(arg=None):
    """
    A simple function that accepts an optional argument.
    If the argument is None, it returns 0, otherwise it returns the argument.
    """
    if arg is None:
        return 0
    else:
        return arg

# Demonstrating the usage of None and my_function
num1 = 5
result1 = my_function(num1)
print("Result for num1 = {}: {}".format(num1, result1))

num2 = None
result2 = my_function(num2)
print("Result for num2 = None: {}".format(result2))

# Demonstrating the usage of import and math.sqrt
num3 = 4
square_root = math.sqrt(num3)
result3 = my_function(square_root)
print("Result for square root of num3: {}".format(result3))
