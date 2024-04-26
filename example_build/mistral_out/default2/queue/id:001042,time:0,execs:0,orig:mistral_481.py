
# Define a function that takes an argument and sets it to None if no argument is provided
def set_to_none(arg=None):
    print("Original arg:", arg)
    if arg is None:
        arg = None
    else:
        arg = 42
        print("Argument assigned a new value: ", arg)

    print("Function argument after the function call: ", arg)

# Call the function with an argument
set_to_none(3)
print()

# Call the function without an argument
set_to_none()
