
# A simple Python program demonstrating the use of None
def greet(name=None):
    if name is None:
        print("Hello, Stranger!")
    else:
        print(f"Hello, {name}!")

greet() # prints "Hello, Stranger!"
greet("John Doe") # prints "Hello, John Doe!"
