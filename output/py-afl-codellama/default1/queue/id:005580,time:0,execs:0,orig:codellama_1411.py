#!/usr/bin/env python3

def greet(name):
    """A function to greet a person by name."""
    assert name, "Name is required"  # Check if the name is provided
    print("Hello,", name)

greet("Alice")  # This will print "Hello, Alice"
greet(None)  # This will raise an AssertionError because None is not a valid name