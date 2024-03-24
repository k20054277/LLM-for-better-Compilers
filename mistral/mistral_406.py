
def greet(name=None):
    if name is None:
        print("Hello, you haven't provided a name")
        name = input("Please enter your name: ")
        print(f"Hi {name}! Nice to meet you.")
    else:
        print(f"Hello, {name}!")

# Call the function with an argument
greet("Alice")

# Call the function without an argument
greet()
