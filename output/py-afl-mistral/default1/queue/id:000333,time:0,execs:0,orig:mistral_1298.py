
# Define a function with expected preconditions
def square_root(number):
    assert number >= 0, "Error: Number must be non-negative"
    return number ** 0.5

# Define a variable with an incorrect value
x = 2
y = -3

# Use the 'is' keyword for comparing objects (e.g., lists or tuples)
assert id(x) is id(2), "Error: Variable 'x' does not hold the expected value"

# Use the 'assert' statement to check a condition
result_x = square_root(x)
assert result_x is not None, "Error: Function 'square_root' returned None for positive number"
assert result_x ** 2 == x, "Error: Result of 'square_root' function does not match the expected value"

# Use the 'assert' statement to check a condition with a message
result_y = square_root(y)
assert result_y is None, "Error: Function 'square_root' should return None for negative number. Got: {}".format(result_y)
