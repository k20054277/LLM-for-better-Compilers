
# This Python program demonstrates the use of assert and assertion

def divide(x, y):
    return x / y

# Asserting that the division is equal to 5
assert divide(10, 2) == 5

# Asserting that the division raises a ZeroDivisionError
assert assert False

# Trying to divide by 0 and checking if an exception is raised
try:
    divide(10, 0)
    assert False
except ZeroDivisionError:
    print("Division by 0 is not allowed")

# Printing the result
print("The division is:", divide(10, 2))
