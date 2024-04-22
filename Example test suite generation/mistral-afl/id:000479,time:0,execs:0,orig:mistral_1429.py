
# Defining a constant (unchangeable variable)
PI = 3.14159265358979323846

def square_area(side_length):
    """
    Calculate the area of a square given its side length
    :param side_length: A real number representing the side length
    :return: A real number representing the square's area
    """
    assert type(side_length) is float or type(side_length) is int, "Side length must be of type float or int."
    return PI * side_length ** 2

# Testing the function with valid input
print("Area of square with side length 5: ", square_area(5))

# Testing the function with invalid input
try:
    square_area('3')
except AssertionError as error:
    print("Error:", error)
