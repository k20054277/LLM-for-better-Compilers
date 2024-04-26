
# This Python program demonstrates the use of assert and lambda

def square(x):
    return x ** 2

# Asserting that square(5) is equal to 25
assert square(5) == 25

# Lambda expression to square a number
square_lambda = lambda x: x ** 2

# Asserting that square_lambda(6) is equal to 36
assert square_lambda(6) == 36

# Printing the results
print("The value of square(5) is:", square(5))
print("The value of square_lambda(6) is:", square_lambda(6))
