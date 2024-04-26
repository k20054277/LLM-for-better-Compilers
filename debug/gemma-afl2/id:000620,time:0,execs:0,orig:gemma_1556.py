
# This Python program demonstrates the use of assert and raise

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

# Asserting a condition
assert divide(5, 2) == 2.5

# Asserting an exception
assert raise ZeroDivisionError("Cannot divide by zero") == divide(5, 0)

# Raising an exception
try:
    divide(5, 0)
except ZeroDivisionError as e:
    print(e)
    assert str(e) == "Cannot divide by zero"
