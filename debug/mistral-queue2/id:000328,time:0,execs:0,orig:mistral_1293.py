
import math

# Define a simple function 'add' that takes two arguments and returns their sum
def add(num1, num2):
    """
    Function to add two numbers and return the sum.

    :param num1: The first number
    :param num2: The second number
    :return: The sum of 'num1' and 'num2'
    """
    result = num1 + num2
    assert type(num1) is (int or float), "The first argument must be either integer or float."
    assert type(num2) is (int or float), "The second argument must be either integer or float."
    return result

# Import 'pi' constant from the math module
from math import pi

if __name__ == "__main__":
    # Test the function with valid inputs
    print(f"The sum of 2 and 3 is: {add(2, 3)}")

    # Test the function with invalid input (non-numeric)
    try:
        result = add("1", 3)
        assert False, "This should not be reached."
    except AssertionError as error:
        print(f"Error: {error}")

    # Perform some calculations using 'pi'
    radius = 5.0
    area = pi * (radius ** 2)
    circumference = 2 * pi * radius
    print(f"Area of the circle with a radius of 5 is: {area}")
    print(f"Circumference of the circle with a radius of 5 is: {circumference}")
