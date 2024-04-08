def greet(name):
    print("Hello, " + name)

greet("Alice") # Outputs: Hello, Alice
greet("Bob")   # Outputs: Hello, Bob

# Using the and operator with a method call
if greet("Alice") and greet("Bob"):
    print("Both functions returned True")