
# Function that takes an optional parameter with default value as None
def greet(name=None):
    if name is not None:
        print("Hello, " + name)
    else:
        print("Hello, World!")
        
# Calling the function without any argument
greet()
# Output: Hello, World!

# Calling the function with an argument
greet("Alice")
# Output: Hello, Alice
