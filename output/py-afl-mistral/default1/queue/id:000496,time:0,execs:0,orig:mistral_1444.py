
def add(x, y):
    assert x is not None, "x must be provided"
    assert y is not None, "y must be provided"
    return x + y

add(3, 5)
add(None, 5)
