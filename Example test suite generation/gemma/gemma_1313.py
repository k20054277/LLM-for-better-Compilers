
# This Python program demonstrates the use of as and ()

# Define a function called square
def square(x):
    return x ** 2

# Use as to bind the square function to the variable y
y = square

# Use parentheses to call the square function
z = square(5)

# Print the values of y and z
print(y(2))
print(z)
