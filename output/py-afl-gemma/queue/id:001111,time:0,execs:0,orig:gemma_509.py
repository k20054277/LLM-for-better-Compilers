
# Define a function that returns None
def greet(name):
    if name is None:
        return None

    return "Hello, " + name


# Test the function with different inputs
print(greet(None))  # Output: None
print(greet("John"))  # Output: Hello, John
print(greet("Jane"))  # Output: Hello, Jane

# Check if the function returns None
print(greet(None) is None)  # Output: True
