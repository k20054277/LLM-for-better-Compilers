def greet(name):
    if name == "Alice":
        return "Hello, Alice!"
    elif name == "Bob":
        return "Hello, Bob!"
    else:
        return "Hello, {0}!".format(name)

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob"))    # Output: Hello, Bob!
print(greet("Charlie")) # Output: Hello, Charlie!