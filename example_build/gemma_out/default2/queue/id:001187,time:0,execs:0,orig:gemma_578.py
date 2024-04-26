
# This Python program demonstrates the use of None and is

# Define a function that returns None
def my_function():
    return None

# Check if the function returns None
if my_function() is None:
    print("The function returned None")

# Check if the function returns None or a boolean value
if my_function() is None or False:
    print("The function returned None or False")

# Output
# The function returned None
# The function returned None or False
