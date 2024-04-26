# This program demonstrates the use of None and syntax in Python

# Printing None:
print(None)  # Outputs "None"

# Syntax for using None as an argument:
def greet(name):
    if name is None:
        print("Hello, there!")
    else:
        print(f"Hello, {name}!")

greet(None)  # Outputs "Hello, there!"
greet("Alice")  # Outputs "Hello, Alice!"