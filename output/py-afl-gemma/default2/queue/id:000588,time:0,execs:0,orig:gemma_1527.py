
# This Python program demonstrates the use of assert and /.

def divide(x, y):
    return x / y

# Asserting that the division is equal to 5
assert divide(10, 2) == 5

# Asserting that the division is greater than 4
assert divide(10, 2) > 4

# Trying to divide by 0 raises a ZeroDivisionError
try:
    assert divide(10, 0) == 10
except ZeroDivisionError:
    print("Division by 0 is not allowed")

# Printing the result
print("The division is:", divide(10, 2))
