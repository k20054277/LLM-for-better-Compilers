
# This Python program demonstrates the use of as and or

# Define a function called greet
def greet(name):
    print("Hello, " + name + "!")

# Get the user's name
name = input("What is your name? ")

# Greet the user
greet(name)

# If the user does not provide a name, use the default name "John Doe"
if not name:
    name = "John Doe"
    greet(name)

# Print a message
print("Thank you for visiting, " + name + "!")
