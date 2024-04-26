
# Demonstrating the use of AS and **=

# Define a function
def square(x):
    return x ** 2

# Assign the square function to the variable y
y = square

# Use the as keyword to bind the square function to the variable z
z = square as sq

# Use the double assignment operator to assign the square function to the variable w
w = square **=

# Print the values of y, z, and w
print(y(5))
print(z(6))
print(w(7))
