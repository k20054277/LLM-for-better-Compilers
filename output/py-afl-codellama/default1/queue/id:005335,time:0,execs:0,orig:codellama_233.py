# Demonstrate the use of False and vars() in Python

# Define a variable with a value of True
my_bool = True

# Use the vars() function to get a dictionary of all variables in the current scope
vars = vars()

# Print the contents of the vars dictionary
print(vars)

# Set the value of my_bool to False using the assignment operator
my_bool = False

# Print the updated value of my_bool
print(my_bool)

# Use the vars() function again to get a dictionary of all variables in the current scope
new_vars = vars()

# Check if the variable "my_bool" is in the new_vars dictionary
if "my_bool" in new_vars:
    print("The variable 'my_bool' has been updated")
else:
    print("The variable 'my_bool' has not been updated")