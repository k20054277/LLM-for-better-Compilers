
# This Python program demonstrates the use of as and %.

# Define a function called greet.
def greet(name):
    print("Hello, " + name + "!")

# Use the as keyword to assign the function object to the variable greet_function.
greet_function = greet

# Use the % operator to format the string.
print(f"The function greet returns the greeting: {greet_function('John Doe')}")
