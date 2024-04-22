
# Define a function that takes one argument which can be optional
def greet(name=None):
    if name is None:
        print("Hello! What's your name?")
        name = input("Your name: ")
    print(f"Hello, {name}!")

# Call the function with no argument to see it asking for a name
greet()

# Or call the function with an argument to greet directly
greet("Alice")
