
# This Python program demonstrates the use of assert and error

def divide(x, y):
    # Asserting that y is not equal to 0
    assert y != 0

    # Dividing x by y
    result = x / y

    # Returning the result
    return result

# Trying to divide by 0
try:
    divide(10, 0)
except ZeroDivisionError:
    print("Cannot divide by 0")

# Output
# Cannot divide by 0
