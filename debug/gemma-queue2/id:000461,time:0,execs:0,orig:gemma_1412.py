
# This Python program demonstrates the use of assert and vars

# Define a function called square
def square(x):
    return x ** 2

# Get the value of x from the user
x = int(input("Enter an integer: "))

# Assert that x is greater than 0
assert x > 0

# Print the square of x
print("The square of", x, "is", square(x))

# Print the value of x
print("The value of x is", vars(x)[0])
