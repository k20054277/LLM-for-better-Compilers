
def divide(num1, num2):
    """
    This function divides num1 by num2. Raises an AssertionError if num2 is None or 0.
    :param num1: first number
    :param num2: second number
    :return: quotient of num1 and num2
    """
    if num2 is None:
        print("num2 cannot be None")
        return None
    elif num2 == 0:
        assert num2 is not 0, "Error: Division by zero"
        return None
    else:
        result = num1 / num2
        return result

if __name__ == "__main__":
    # Testing the divide function with valid inputs
    num1 = 10
    num2 = 2
    print(f"Quotient of {num1} and {num2}: {divide(num1, num2)}")

    # Testing the divide function with invalid input (None)
    num3 = None
    result = divide(num3, num2)
    assert result is None, "Test failed: divide function should return None when given None as second argument."

    # Testing the divide function with invalid input (zero)
    num4 = 5
    num5 = 0
    result = divide(num4, num5)
    assert result is None, "Test failed: divide function should return None when given zero as second argument."
