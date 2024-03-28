
# This Python program demonstrates the use of as and /.

# Define a function called my_function.
def my_function(x):
    return x * 2

# Assign the return value of my_function to the variable y.
y = my_function(5)

# Print the value of y.
print(y)

# Use the as keyword to assign the return value of my_function to the variable z.
z = my_function(5) as h

# Print the value of z and h.
print(z)
print(h)
