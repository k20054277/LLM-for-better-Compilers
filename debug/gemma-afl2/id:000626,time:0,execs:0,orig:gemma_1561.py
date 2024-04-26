
# This Python program demonstrates the use of assert and raise

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

# Asserting a condition
assert divide(5, 2) == 2.5

# Asserting an exception
assert raise ZeroDivisionError(divide(5, 0))

# Trying to assert an exception that doesn't occur
try:
    assert divide(5, 0) == 2.5
except ZeroDivisionError:
    print("Expected exception occurred")

# Output
# Expected exception occurred
