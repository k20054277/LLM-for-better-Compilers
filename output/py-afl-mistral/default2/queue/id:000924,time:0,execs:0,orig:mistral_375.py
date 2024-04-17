
# This example shows how to use None as a default value for function arguments

def my_function(arg1=None, arg2=None):
    """This function demonstrates the use of None as a default value for function arguments."""
    if arg1 is None:
        print("Argument 'arg1' was not provided.")
    else:
        print("Argument 'arg1' has the value:", arg1)

    if arg2 is None:
        print("Argument 'arg2' was not provided.")
    else:
        print("Argument 'arg2' has the value:", arg2)

# Call the function with no arguments
my_function()

# Call the function with one argument
my_function("value1")

# Call the function with two arguments
my_function("value1", "value2")
