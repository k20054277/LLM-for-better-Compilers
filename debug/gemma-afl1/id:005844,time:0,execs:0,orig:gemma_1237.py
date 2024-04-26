
# This Python program demonstrates the use of the as and syntax.

# Define a function called my_function.
def my_function(x):
    return x * x

# Assign the return value of my_function to the variable y.
y = my_function(5)

# Print the value of y.
print(y)

# Output: 25

# The as syntax is used to assign a temporary variable to the return value of a function call.
y_as_temp = my_function(5)

# Print the value of y_as_temp.
print(y_as_temp)

# Output: 25
