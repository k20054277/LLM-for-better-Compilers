
def my_function(param1, param2=None):
    """This function takes two parameters: param1 and param2.

    param1 is required, while param2 is optional.

    The function returns None.
    """

    print("param1:", param1)
    print("param2:", param2)

    return None


# Call the function with a single parameter
my_function(10)

# Call the function with two parameters
my_function(10, 20)
