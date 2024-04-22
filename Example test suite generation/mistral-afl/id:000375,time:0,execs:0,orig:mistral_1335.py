
def add_numbers(a, b):
    """
    Add two numbers and returns the sum.
    :param a: First number
    :param b: Second number
    :return: The sum of a and b
    """
    result = a + b
    assert result == (a + b), f"Error! Expected {a + b}, but got {result}"
    return result

if __name__ == "__main__":
    x = 3
    y = 4
    z = add_numbers(x, y)
    print("The sum of {} and {} is {}".format(x, y, z))
