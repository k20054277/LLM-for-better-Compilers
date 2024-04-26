
# True and exec

# Define a function
def my_function():
    print("Hello, world!")

# Check if the function is True
if my_function() is True:
    print("The function returned True")

# Execute the function using exec
exec(my_function.__name__)

# Output
# Hello, world!
# The function returned True
