
def demo(obj, attr):
    """Demonstrates the use of as and getattr."""

    # Use as to bind a temporary variable to an attribute
    as_attr = getattr(obj, attr)

    # Use getattr to get an attribute from an object
    print(getattr(obj, attr))

    # Use as and getattr to access and modify an attribute
    as_attr += 10

    # Print the modified attribute
    print(getattr(obj, attr))


# Example usage
demo(my_object, "name")
