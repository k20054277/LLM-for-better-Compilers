
# Assigning None to a variable
x = None
print(x)  # Output: None

# Using None as a default value for function arguments
def print_value(value=None):
    if value is not None:
        print(value)

# Call the function with and without an argument
print_value()
print_value("Hello, World!")
