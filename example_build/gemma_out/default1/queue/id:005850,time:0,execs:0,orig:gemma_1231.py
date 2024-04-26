
# Import the as module
import as

# Define a function
def my_function(x):
    return x**2

# Assign the function to a variable
my_function_alias = as.function(my_function)

# Use the alias to call the function
print(my_function_alias(5))

# Print the original function
print(my_function(5))
