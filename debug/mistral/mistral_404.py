
# Define a constant called MAX_LIMIT with value 100
MAX_LIMIT = 100

def function_with_none():
    """
    This function demonstrates the use of None.
    """
    # Assigning None to a variable
    none_value = None

    print("None Type: ", type(none_value))

    # Function with a parameter that can accept None
    def another_function(param):
        if param is None:
            print("Parameter is None")
        else:
            print("Parameter has a value:", param)

    # Calling another function with None and non-None values
    another_function(None)
    another_function("Hello World")

# Calling the function_with_none()
function_with_none()
