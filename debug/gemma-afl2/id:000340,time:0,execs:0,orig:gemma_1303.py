
# This Python program demonstrates the use of as and << operators

# Define a function called greet
def greet(name):
    print("Hello, " + name + "!")

# Assign the greet function to the as variable func
as func

# Use the func variable to call the greet function
func("John")

# Use the as operator to assign a new name to the function object
func = greet

# Call the greet function using the new name
func("Jane")

# Use the << operator to compare the function object to another function object
print(func == greet)

# Output
# Hello, John!
# Hello, Jane!
# True
