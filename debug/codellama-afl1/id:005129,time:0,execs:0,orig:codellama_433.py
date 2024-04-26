def greet(name):
    if name == 'Alice':
        return "Hello, Alice!"
    elif name == 'Bob':
        return "Hello, Bob!"
    else:
        return None

print(greet('Alice'))  # Output: Hello, Alice!
print(greet('Bob'))  # Output: Hello, Bob!
print(greet('Charlie'))  # Output: None