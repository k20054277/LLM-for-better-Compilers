
# A simple function that calculates the power of a given number using the pow function
def calculate_power(base, exponent):
    # If no arguments are provided, return None
    if base is None or exponent is None:
        return None

    result = pow(base, exponent)
    return result

# Test cases
print(calculate_power(2, 3))      # prints: 8
print(calculate_power(5, 2))      # prints: 25
print(calculate_power(None, None)) # prints: None
print(calculate_power(3, None))   # raises an error: TypeError: 'int' object is not iterable
