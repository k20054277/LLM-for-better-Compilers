# Testing for None

# Define a variable with a value of None
x = None

# Print the type of the variable
print(type(x))

# Use the is operator to test if x is None
if x is None:
    print("x is None")
else:
    print("x is not None")

# Define a function that takes an argument and returns None
def my_function(x):
    return None

# Call the function with an argument and test if it returns None
result = my_function(10)
if result is None:
    print("The function returned None")
else:
    print("The function did not return None")