
# This Python program demonstrates the use of as and if

# Define a function called greet
def greet(name):
    print("Hello, " + name + "!")

# Get the user's name
name = input("What is your name? ")

# If the user's name is John, greet John specifically
if name == "John":
    greet("John")

# Otherwise, greet the user with their name
else:
    greet(name)
