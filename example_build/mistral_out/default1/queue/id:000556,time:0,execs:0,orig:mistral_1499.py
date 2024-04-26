
def validate_input(user_input):
    """
    Function to validate user input should be greater than or equal to 0.
    Raise AssertionError if condition is not met.
    """
    assert user_input <= 10, "User input must be less than or equal to 10."
    assert user_input >= 0, "User input must be non-negative."

# Test the validate_input function with valid and invalid inputs
try:
    validate_input(-5)
except AssertionError as error_message:
    print(error_message)

validate_input(3)
validate_input(11)
