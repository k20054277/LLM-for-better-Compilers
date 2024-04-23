
def add(x, y):
    """
    This function adds two numbers and returns the sum.
    :param x: first number
    :param y: second number
    :return: sum of x and y
    """
    result = x + y
    assert type(x) is (int or float), "First argument must be either integer or float"
    assert type(y) is (int or float), "Second argument must be either integer or float"
    return result

# Testing the function with valid inputs
print("Addition of 2 integers: ", add(2, 3))
print("Addition of 2 floats: ", add(2.5, 3.7))

# Testing the function with invalid inputs
try:
    print("Addition of integer and string: ", add(2, "three"))
except AssertionError as e:
    print("Error message:", e)

try:
    print("Addition of float and list: ", add(2.5, [1, 2, 3]))
except AssertionError as e:
    print("Error message:", e)
