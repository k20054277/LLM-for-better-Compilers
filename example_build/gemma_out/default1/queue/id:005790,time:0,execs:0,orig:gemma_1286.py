
# Demonstration of as and =

# Define a function
def square(x):
    return x ** 2

# Assign a variable to the function
y = square(5)

# Use as to bind the function to a new name
as cube = square

# Use = to assign the return value of the function to the variable
z = cube(6)

# Print the values
print(y)
print(z)
