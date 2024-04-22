# Define a function with no parameters
def greet(name):
    # Use "as" to specify the type of variable
    name_str = str(name)
    if name_str == '':
        # Use "pass" to do nothing and continue with the next line
        pass
    else:
        print("Hello, " + name_str)

# Call the function with different values for the parameter
greet('')  # Output: None (because of pass)
greet(123)  # Output: Hello, 123
greet('John')  # Output: Hello, John