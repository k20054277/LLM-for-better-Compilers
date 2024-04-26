
def remove_attr(attr):
    """Removes an attribute from a class.

    Args:
        attr: The attribute to remove.

    Raises:
        AttributeError: If the attribute does not exist.
    """

    assert hasattr(self, attr)  # Assert that the attribute exists.
    delattr(self, attr)  # Delete the attribute.
