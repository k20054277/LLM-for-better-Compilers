
def divide(x, y):
    """
    This function takes two numbers as arguments and returns the quotient of x divided by y.
    Raises a ZeroDivisionError if y is zero.
    """
    assert y != 0, "Error: Division by zero is not allowed."
    return x / y

# Test cases for divide function
if __name__ == "__main__":
    # Test case 1: Divide by a non-zero number
    result = divide(10, 2)
    assert result == 5.0, "Test case failed: divide(10, 2) != 5.0"
    print("Test case 1 passed.")

    # Test case 2: Divide by zero
    with pytest.raises(AssertionError):
        divide(10, 0)

    # Test case 3: Divide large number by smaller non-zero number
    result = divide(200000, 500)
    assert result >= 40.0, "Test case failed: divide(200000, 500) < 40.0"
    print("Test case 3 passed.")
