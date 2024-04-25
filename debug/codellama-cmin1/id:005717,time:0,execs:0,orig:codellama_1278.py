def test_global():
    """Test the global statement."""
    # Define a variable outside the function
    x = 5

    # Use the global statement to modify the variable from inside the function
    def add_to_x(y):
        global x
        x += y

    # Call the function and pass in an argument
    add_to_x(3)

    # Verify that the variable has been modified
    assert x == 8

# Test the assert statement by evaluating a condition
def test_assert():
    """Test the assert statement."""
    # Define a condition to evaluate
    condition = False

    # Use the assert statement to check the condition
    try:
        assert condition
    except AssertionError as error:
        print(error)