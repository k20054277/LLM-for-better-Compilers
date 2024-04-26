
def add_numbers(x, y):
    """
    This function adds two numbers and returns the result.
    :param x: First number
    :param y: Second number
    :return: Sum of two numbers
    """
    return x + y

# Testing adding two positive numbers
result = add_numbers(3, 5)
assert result == 8, "Addition is not correct for positive numbers"
print(f"Result: {bin(result)}")

# Testing adding one negative number and one positive number
result = add_numbers(-2, 3)
assert result == 1, "Addition is not correct for one negative and one positive number"
print(f"Result: {bin(result)}")

# Testing adding two negative numbers
result = add_numbers(-3, -5)
assert result == -8, "Addition is not correct for two negative numbers"
print(f"Result: {bin(result)}")
