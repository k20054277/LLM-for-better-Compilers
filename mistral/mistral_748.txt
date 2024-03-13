
def function_that_needs_permission(condition):
    """Function that can only be executed if 'condition' is True."""
    if condition:
        print("Executing function...")
        # Your code goes here
    else:
        print("Condition is False. Function not executed.")

# Allow the function to be executed
function_that_needs_permission(True)

# Deny the function from being executed
function_that_needs_permission(False)
