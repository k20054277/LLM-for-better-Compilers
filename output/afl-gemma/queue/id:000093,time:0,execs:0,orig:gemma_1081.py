
# This Python program demonstrates the use of as and else

# Define a function called greet
def greet(name):
    # If the name is Alice, return a greeting with the name
    if name == "Alice":
        return "Hello, Alice!"
    # Otherwise, return a greeting with the name and the word "Welcome"
    else:
        return "Hello, " + name + "!"

# Get the name of the person to greet
name = input("What is your name? ")

# Greet the person
greeting = greet(name)

# Print the greeting
print(greeting)
