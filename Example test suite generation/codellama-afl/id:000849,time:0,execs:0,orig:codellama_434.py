# This function returns None if it encounters an error, otherwise it returns the result of the calculation
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        # If the division by zero occurs, return None instead of raising an exception
        return None

# Test the function with some input values
print(divide(10, 5))  # Output: 2
print(divide(10, 0))  # Output: None