
# This Python program demonstrates the use of None and statement

# Define a function
def my_function(x):
    # If x is None, return None
    if x is None:
        return None

    # Otherwise, return x squared
    else:
        return x ** 2

# Get the value of x
x = None

# Call the function
result = my_function(x)

# Check if the function returned None
if result is None:
    print("The function returned None")

# Otherwise, print the result
else:
    print("The function returned:", result)
