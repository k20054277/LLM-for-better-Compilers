
def is_positive(number):
    """
    This function checks if a given number is positive, and returns True if it is, otherwise False.
    :param number: an integer or float
    :return: Boolean value (True or False)
    """

    # Check if the given number is greater than zero
    if number > 0:
        result = True
    else:
        result = False
    
    # Return the result
    return result

# Test some numbers
print(is_positive(5))      # Expected output: True
print(is_positive(-3))      # Expected output: False
print(is_positive(0))      # Expected output: False
