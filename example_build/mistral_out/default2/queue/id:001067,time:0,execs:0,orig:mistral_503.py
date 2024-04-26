
def validate_input(user_input):
    """
    Validate user input is an integer within a specified range.
    :param user_input: The input provided by the user.
    :return: None if valid, raises AssertionError if not.
    """

    # Set minimum and maximum values
    min_value = 1
    max_value = 5

    try:
        # Convert user input to an integer
        num = int(user_input)

        # Check if the number is within the specified range
        if num >= min_value and num <= max_value:
            print("Input is valid.")
            return
        else:
            print(f"Input should be between {min_value} and {max_value}.")

        # Raise an AssertionError if the number is not valid
        assert num >= min_value and num <= max_value, "Invalid input. Number should be between {} and {}.".format(min_value, max_value)
    except ValueError:
        print("Invalid input. Please provide a valid integer.")

# Get user input
user_input = input("Enter an integer between 1 and 5: ")

# Validate user input
validate_input(user_input)
