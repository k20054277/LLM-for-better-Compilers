
# This Python program demonstrates the use of assert and ()

def divide(x, y):
    return x / y

# Asserting that the division of x and y is equal to 5
assert divide(10, 2) == 5

# Asserting that the division of x and y is not equal to 6
assert divide(10, 2) != 6

# Printing the result of the division
print(divide(10, 2))
