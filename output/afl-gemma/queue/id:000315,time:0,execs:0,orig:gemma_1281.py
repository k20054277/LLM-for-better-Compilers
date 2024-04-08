
# Demonstrating the use of as and *

# Define a function
def multiply(x, y):
    return x * y

# Assign a variable to the function
my_function = multiply

# Use as to create an alias for the function
as_function = multiply

# Use * to unpack the function's arguments
args = 5, 10

# Call the function using the alias
as_function(*args)

# Call the function using the unpack
my_function(*args)

# Print the result
print(as_function(*args))
print(my_function(*args))
