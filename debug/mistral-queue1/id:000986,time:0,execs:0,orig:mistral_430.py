
def double(number):
    """
    This function takes one argument and returns the double of that number.
    If the input is None, an AssertionError is raised.
    """
    if number is None:
        assert number is not None, "Input can't be None"
        raise AssertionError("Input can't be None")
     return number * 2

# Testing the function with valid and invalid inputs
print(double(3))               # Output: 6
print(double(None))             # Raises an AssertionError with message "Input can't be None"
