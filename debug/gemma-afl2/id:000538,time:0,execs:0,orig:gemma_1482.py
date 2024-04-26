
# This Python program demonstrates the use of assert and syntax

# Define a function called square
def square(x):
    return x ** 2

# Assert that square(5) is equal to 25
assert square(5) == 25

# Print the result
print("The square of 5 is:", square(5))

# This syntax error will occur
# assert square(10) is not equal to 100

# Print an error message
print("Syntax error:", square(10) is not equal to 100)
