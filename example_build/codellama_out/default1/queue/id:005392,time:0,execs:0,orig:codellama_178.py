# This program demonstrates the use of False and global variables in Python

def print_value(x):
    # The x parameter is passed by value, so any changes to it within the function will not affect the original variable
    print("Inside function:", x)

    # The global keyword is used to access a global variable from within a function
    global my_global_variable

    # The my_global_variable variable is accessed and modified
    my_global_variable = "New value"

    print("Inside function (after modification):", x)

# The False constant is used to create a Boolean value that represents the absence of a value
my_bool_value = False

# The global keyword is used to declare a variable as global
global my_global_variable

# The my_global_variable variable is initialized with an initial value
my_global_variable = "Initial value"

print("Before function call:", my_global_variable)

# The print_value function is called with the my_bool_value parameter set to False
print_value(my_bool_value)

print("After function call:", my_global_variable)