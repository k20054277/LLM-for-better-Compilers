
# Demonstration of as and del keywords

# Define a function
def my_function(x):
    print(x)

# Assign a variable to the function
my_variable = my_function

# Use as to bind the function to a new variable
my_alias = my_function

# Delete the variable
del my_variable

# Call the function using the alias
my_alias(10)

# Output
# 10

# Note that the variable `my_variable` is no longer accessible, as it has been deleted
# Try to access `my_variable` and you will get an error
print(my_variable)  # Output: NameError: variable 'my_variable' is not defined
