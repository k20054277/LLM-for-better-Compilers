
# This Python program demonstrates the use of and and else

# Define a function called 'check_status'
def check_status(status):
    # If the status is active, return True
    if status == 'active':
        return True
    # Otherwise, return False
    else:
        return False

# Get the status of a user
user_status = 'active'

# Check if the user's status is active
if check_status(user_status):
    # Print "The user is active."
    print("The user is active.")
else:
    # Print "The user is not active."
    print("The user is not active.")
