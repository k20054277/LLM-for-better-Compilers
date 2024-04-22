
# Assigning None to a variable
my_variable = None
print("Value of my_variable:", my_variable)

# Check if a variable is equal to None
another_variable = "Some value"
if another_variable is None:
    print("another_variable is None")
else:
    print("another_variable has a value:", another_variable)

# Function that returns None as default value
def my_function():
    pass

# Calling the function and storing its result in a variable
result = my_function()
print("Value of result:", result)
