
# Define some variables
var1 = 10
var2 = "Hello"

# Check if a variable is defined and its value is false
if not var1 or (var2 and var2 == ""):
    print("One of the variables is not defined or has a false value.")
else:
    print("Both variables are defined and have non-false values.")

# Get the dictionary of current variables
variables = vars()
print("Current variables:")
print(variables)

# Assign a false value to a variable
variables["var3"] = False
print("Updated variable with a false value:")
print(variables)
