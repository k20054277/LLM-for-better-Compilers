# This program demonstrates the use of None and continue

while True:
    # Get input from the user
    user_input = input("Enter a value: ")

    if user_input == "None":
        # Set the variable to None
        none_var = None
    else:
        # Convert the input to an integer
        try:
            int_value = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue  # Go back to the beginning of the loop

    # Check if the variable is None
    if none_var is not None:
        # Print the value of the variable
        print(f"The value of none_var is {none_var}")
    else:
        # If the variable is None, print a message
        print("None was entered.")