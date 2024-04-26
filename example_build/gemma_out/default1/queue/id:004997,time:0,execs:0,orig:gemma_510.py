
"""Demonstrating use of None and documentation

"""

def greet(name, greeting = None):
    """Greets a person with a specified greeting.

    If no greeting is provided, the default greeting is "Hello".

    Args:
        name: The person's name.
        greeting: An optional greeting.

    Returns:
        A greeting message.
    """

    if greeting is None:
        greeting = "Hello"

    return f"Greetings, {name}. {greeting}"

print(greet("John"))
print(greet("John", "Welcome"))
print(greet("Jane"))
print(greet("Jane", "Good morning"))
