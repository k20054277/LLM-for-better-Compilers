# This program demonstrates the use of "as" and debugging in Python

# Import the necessary modules
import pdb

# Define a function to be debugged
def my_function(x):
    # Perform some computation using x
    result = x * 2 + 3
    return result

# Use the pdb module to enable debugging for my_function()
pdb.set_trace()

# Call my_function() with a value of 5
result = my_function(5)

# Print the result of my_function()
print(result)