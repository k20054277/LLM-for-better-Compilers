
# This Python program demonstrates the use of assert and debugging

def divide(x, y):
    # Assert that y is not equal to 0
    assert y != 0
    # Divide x by y
    return x / y

# Try to divide 10 by 0
try:
    divide(10, 0)
except ZeroDivisionError:
    print("Error: division by zero is not allowed")

# Print the result
print("The result is:", divide(10, 2))
