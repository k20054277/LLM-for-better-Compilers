
def demo(obj, attr):
    """Demonstrates the use of and and getattr."""

    # Check if the attribute exists on the object.
    if hasattr(obj, attr):
        # Get the value of the attribute.
        value = getattr(obj, attr)

        # Print the value of the attribute.
        print("The value of the attribute %s is %s." % (attr, value))


# Create an object.
my_object = {"name": "John Doe", "age": 30}

# Demonstrate the use of and and getattr.
demo(my_object, "name")
demo(my_object, "age")

# Output:
# The value of the attribute name is John Doe.
# The value of the attribute age is 30.
