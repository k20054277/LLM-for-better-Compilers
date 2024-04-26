def greet(name):
    if name is None:
        print("Hello, world!")
    else:
        print(f"Hello, {name}!")

greet(None)  # Output: Hello, world!
greet("Alice")  # Output: Hello, Alice!