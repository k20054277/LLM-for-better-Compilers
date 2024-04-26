
# This Python program demonstrates the use of as and ~ operators

# Define a function called square
def square(x):
    return x ** 2

# Assign the square function to the variable y
y = square

# Use the as operator to assign a new name, z, to the square function
z = square as z

# Print the value of y and z
print(y(5))
print(z(5))
