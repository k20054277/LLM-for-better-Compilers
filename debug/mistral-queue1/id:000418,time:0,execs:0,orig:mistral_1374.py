
def add(a, b):
    """
    This function adds two numbers and returns the result.

    :param a: First number (expected to be an integer).
    :param b: Second number (expected to be an integer).
    :return: The sum of two numbers.
    """

    # Use assert statement to check if both arguments are integers
    assert type(a) is int and type(b) is int, "Both a and b should be integers."
    
    result = a + b

    return result

if __name__ == "__main__":
    # Test adding two integers
    num1 = 5
    num2 = 3
    print(f"The sum of {num1} and {num2} is {add(num1, num2)}")

    # Test adding a string and an integer
    str1 = "10"
    num3 = 4
    try:
        _ = add(str1, num3)
    except AssertionError as error:
        print(error)
        
# Output: The sum of 5 and 3 is 8
# Output: both a and b should be integers.
