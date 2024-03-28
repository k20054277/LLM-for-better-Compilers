
# This Python program demonstrates the use of None and <

# Define a function that returns None
def no_return():
    return None

# Define a function that returns a number
def return_number(x):
    return x

# Print the return value of no_return()
print(no_return())

# Print the return value of return_number(5)
print(return_number(5))

# Check if the return value of no_return() is None
if no_return() is None:
    print("No return value")

# Check if the return value of return_number(5) is not None
if return_number(5) is not None:
    print("Return value is not None")
