
# This Python program demonstrates the use of and and dir functions.

# Define a function called my_function.
def my_function(x, y):
    return x + y

# Get the directory of the my_function function.
my_function_dir = dir(my_function)

# Print the directory of the my_function function.
print("The directory of the my_function function is:")
print(my_function_dir)

# Check if the my_function function has a variable called x.
if "x" in my_function_dir:
    print("The my_function function has a variable called x.")

# Check if the my_function function has a variable called y.
if "y" in my_function_dir:
    print("The my_function function has a variable called y.")

# Call the my_function function with two arguments.
my_function(5, 10)

# Print the result of the function call.
print("The result of the function call is:")
print(my_function(5, 10))
