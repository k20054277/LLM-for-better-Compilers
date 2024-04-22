
# This Python program demonstrates the use of as and <

# Define a function called square
def square(x):
    return x ** 2

# Assign the square function to the variable y
y = square

# Use the as keyword to assign a new name to the function
as cube

# Print the value of cube(5)
print(cube(5))

# Output: 25

# Use the < operator to compare the square function to the identity function
print(square < identity)

# Output: False
