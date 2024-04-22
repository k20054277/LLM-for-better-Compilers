
# Demonstrating the use of as and & in Python

# Define a function called square
def square(x):
    return x ** 2

# Assigning a variable to the square function
square_as = square

# Using the square function with as
print(square_as(5))

# Using the square function with &
print(square(5))

# Output:
# 25
# 25
