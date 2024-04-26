
# This Python program demonstrates the use of None and << operators

# Define a function that returns None
def foo():
    return None

# Define a variable and assign None to it
my_variable = None

# Use None comparison
if my_variable is None:
    print("my_variable is None")

# Use None as a default value for a variable
my_other_variable = None

# Use None in an expression
print(my_variable << 2)  # Output: None

# Use None in a comparison
if my_variable is not None:
    print("my_variable is not None")

# Print the value of my_variable
print(my_variable)  # Output: None

# Print the value of my_other_variable
print(my_other_variable)  # Output: None
