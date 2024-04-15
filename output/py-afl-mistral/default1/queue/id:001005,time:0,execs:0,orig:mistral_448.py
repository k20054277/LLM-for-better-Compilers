
# Define a function with an optional argument, default value is None
def greet(name=None):
    if name is not None:
        print(f"Hello, {name}!")
    else:
        print("Hello there!")

# Call the function with a name argument
greet("Alice")

# Call the function without an argument (it will use the default value of None)
greet()
