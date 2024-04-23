
# This Python program demonstrates the use of as and == operators

# Define a function called greet
def greet(name):
    print("Hello, " + name + "!")

# Assign a variable to the function
my_function = greet

# Use the as operator to assign a new name to the function
my_function_alias = greet

# Check if the function is the same as the alias
if my_function is my_function_alias:
    print("The function is the same.")

# Check if the function's output is the same as the alias
if my_function( "John") == my_function_alias("John"):
    print("The function's output is the same.")

# Output
# Hello, John!
# The function is the same.
# Hello, John!
# The function's output is the same.
