# Demonstrate the use of False and error

# Define a function that takes a boolean argument
def my_function(arg):
    if arg:
        print("Argument is True")
    else:
        print("Argument is False")

# Call the function with different arguments to demonstrate behavior
my_function(True)  # Outputs "Argument is True"
my_function(False)  # Outputs "Argument is False"

# Use error() to raise a custom error message
try:
    my_function(None)
except ValueError as e:
    print("Invalid argument:", e)