
def greet(name):
    """Says hello to a person.

    Args:
        name: The person's name.

    Returns:
        A greeting.
    """

    if name is None:
        return "Hello, stranger!"
    else:
        return "Hello, " + name + "!"

print(greet(None))  # Output: Hello, stranger!
print(greet("John"))  # Output: Hello, John!
