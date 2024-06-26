# Demonstrate the use of None and | in Python

# None is used to represent the absence of a value in Python
x = None
print(x)  # Output: None

# The pipe operator (|) can be used to chain multiple values together
y = x | "hello"
print(y)  # Output: hello

# If none is used as the first argument of a function, it will return the second argument
def greet(name):
    if name is None:
        return "Hello, world!"
    else:
        return f"Hello, {name}!"

print(greet(None))  # Output: Hello, world!
print(greet("Alice"))  # Output: Hello, Alice!