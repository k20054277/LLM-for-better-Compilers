def greet(name):
    print("Hello, " + name)

greet_func = greet

if callable(greet_func):
    greet_func("Alice")  # Output: Hello, Alice

# The following line raises a TypeError because greet is not a function
# greet("Bob")