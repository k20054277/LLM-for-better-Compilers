
# Demonstrating the use of as and :

# Define a function
def greet(name):
    print("Hello, " + name + "!")

# Assigning a variable to the function
my_function = greet

# Calling the function using the variable
my_function("John")

# Using as to bind a variable to the function
as hello_function = greet

# Calling the function using the bound variable
hello_function("Alice")
