
def greet(name="", is_formal=False):
    """
    This function prints a greeting message based on the provided name and formality level.
    :param name: The person's name to greet
    :param is_formal: A Boolean value indicating whether or not to use formal language (default: False)
    """

    if name:
        if is_formal:
            print(f"Good day, {name.capitalize()}.")
        else:
            print(f"Hi, {name}!")
    else:
        print("Please provide a name.")

# Using the default argument values
greet()

# Providing an argument for name but not is_formal
greet("Alice")

# Providing arguments for both name and is_formal
greet("Bob", True)
