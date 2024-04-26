
# This Python program demonstrates the use of None and >

# Define a function that returns None
def no_return():
    return None

# Define a variable and assign it to the function that returns None
my_variable = no_return()

# Check if the variable is None
if my_variable is None:
    print("my_variable is None")

# Compare the variable to a number greater than 10
if my_variable is not None and my_variable > 10:
    print("my_variable is greater than 10")
