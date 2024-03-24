
# Define a function 'my_function' that can return None
def my_function(parameter=None):
    """
    This is a simple Python function that can accept an optional parameter and returns None.
    :param parameter: An optional parameter (default is None)
    :return: None or the given parameter if it is not None
    """
    if parameter is not None:
        return parameter
    else:
        return None

# Call 'my_function' with different arguments
result1 = my_function(42)
print(f"Result 1: {result1}")

result2 = my_function()
print(f"Result 2: {result2}")
