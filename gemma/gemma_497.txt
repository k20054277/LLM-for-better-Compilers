
# Define a function that returns None
def no_return():
    print("I have no return value")
    return None

# Call the function and check if the return value is None
if no_return() is None:
    print("The return value is None")

# Use the None expression
if not no_return():
    print("The function returned something")
