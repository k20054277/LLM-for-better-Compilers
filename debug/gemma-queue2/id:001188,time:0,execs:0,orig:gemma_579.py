
# This Python program demonstrates the use of None and the colon (:).

# Define a function that returns None.
def my_function():
    return None

# Assign None to a variable.
my_variable = None

# Check if the variable is None.
if my_variable is None:
    print("my_variable is None")

# Use None as a default value for a parameter.
def my_other_function(param1, param2=None):
    print("param1:", param1)
    print("param2:", param2)

my_other_function(10)
my_other_function(10, None)
