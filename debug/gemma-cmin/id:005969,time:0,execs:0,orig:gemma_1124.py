
# This Python program demonstrates the use of as and format

# Define a function called greet
def greet(name):
    # Use as to assign the parameter name to the variable person
    person = name

    # Use format to format the string
    message = f"Hello, {person.upper()}. Welcome to the world of Python!"

    # Print the message
    print(message)

# Call the greet function with different names
greet("John")
greet("Jane")
greet("Mike")
