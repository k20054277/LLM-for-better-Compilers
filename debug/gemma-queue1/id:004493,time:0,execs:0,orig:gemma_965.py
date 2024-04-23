
# This Python program demonstrates the use of and and or operators.

# Define a function called check_status.
def check_status(status):
    # Use an and operator to check if the status is both active and online.
    if status["active"] and status["online"]:
        print("The system is active and online.")

    # Use an or operator to check if the status is active or online.
    elif status["active"] or status["online"]:
        print("The system is active or online.")

    # Otherwise, print an error message.
    else:
        print("The system is not active or online.")

# Create a dictionary called status with the following keys and values:
status = {"active": True, "online": False}

# Call the check_status function.
check_status(status)

# Output:
# The system is active or online.
