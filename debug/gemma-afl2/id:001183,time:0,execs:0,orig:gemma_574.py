
# This Python program demonstrates the use of None and and

# Define a function with a default parameter of None
def my_function(x, y=None):
    # Check if y is None
    if y is None:
        print("y is None")
    # Otherwise, print y
    else:
        print("y is not None")

# Call the function with different arguments
my_function(10)
my_function(10, None)
my_function(10, 20)

# Output:
# y is None
# y is None
# y is not None
