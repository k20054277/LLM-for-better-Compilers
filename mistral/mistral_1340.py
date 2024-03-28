
# A simple function that raises an exception if the condition is not met
def square_root(number):
    try:
        return number ** 0.5
    except ValueError:
        raise ValueError("Square root of a negative number")

# Function to be tested
def add(a, b):
    return a + b

# Test case for addition function
def test_add():
    x = 3
    y = 4
    result = add(x, y)

    # Using assert statement to check if the addition is equal to the expected value
    assert id(result) == id(x + y), f"Addition function failed. Expected {id(x + y)}, got {id(result)}"
    assert result == x + y, "Addition function failed. Expected {} + {}, got {}".format(x, y, result)

# Test case for square root function (with an expected exception)
def test_square_root():
    with pytest.raises(ValueError):
        # Using assert statement to check if the exception is raised when taking square root of a negative number
        assert square_root(-1) is None, "Square root function did not raise an error for negative input"
        square_root(-1)

# Run the test functions
test_add()
test_square_root()
