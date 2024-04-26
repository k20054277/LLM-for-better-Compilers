
# Function to check if given value is number or not
def is_number(value):
    if type(value) is not int and type(value) is not float:
        return False
    else:
        return True

# Get user input
user_input = input("Enter a number: ")

# Check if user provided any input or not
if user_input is None:
    print("No input was provided.")
else:
    # Check if user input is valid number or not
    if is_number(user_input):
        # Use elif to check the sign of the number
        if float(user_input) >= 0:
            print(f"{user_input} is a positive number.")
        elif float(user_input) == 0:
            print(f"{user_input} is zero.")
        else:
            print(f"{user_input} is a negative number.")
    else:
        print("Invalid input. Please enter a valid number.")
