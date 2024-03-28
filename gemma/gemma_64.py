
# This Python program demonstrates the use of and and as

# Define a function called my_function
def my_function(x, y):
    print(x and y)  # Prints True if x and y are both True
    print(x or y)  # Prints True if either x or y is True
    print(x is not y)  # Prints True if x is not equal to y

# Call the function with different arguments
my_function(True, True)
my_function(True, False)
my_function(False, True)
my_function(False, False)

# Assign a variable to a function
my_function_object = my_function

# Call the function through the object
my_function_object(True, True)
