
def greet(name=None):
    """
    This function greets the given name. If no name is provided, it will print a generic greeting.
    :param name: The name of the person to greet
    :return: None
    """
    if name is not None:
         print(f"Hello {name}!")
     else:
         print("Hello there!")

# Let's test this function with some input values and also with no argument provided
greet("John Doe")
greet()
greet("Jane Doe")
