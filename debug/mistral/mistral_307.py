
# Function with a default argument value of None
def greet(name=None):
    if name is not None:
        return "Hello, {}!".format(name)
    else:
        return "Hello!"

# Test the function with and without an argument
print(greet("Alice"))  # Hello, Alice!
print(greet())         # Hello!
