
# Function that returns None
def my_function():
    print("This function does not return anything.")
    return None

# Variable with no value assigned
my_variable = None

# Call the function and assign the returned None to a variable
result = my_function()
print(type(result))  # Output: <class 'NoneType'>
