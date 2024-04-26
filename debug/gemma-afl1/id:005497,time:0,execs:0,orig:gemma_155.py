
# This Python program demonstrates the use of and and dir functions

# Define a function called my_function
def my_function(x):
    print(x)

# Check if the function is defined and print its attributes
if my_function is not None and hasattr(my_function, '__doc__'):
    print("Function is defined and has docstring:")
    print(my_function.__doc__)

# Print the directory of attributes for the function
print("Attributes of the function:")
print(dir(my_function))

# Check if the function has a particular attribute
if hasattr(my_function, 'x'):
    print("The function has an attribute called x:")
    print(my_function.x)
