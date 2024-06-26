
# my_module.py
def add(a, b):
    """Add two numbers"""
    return a + b

def is_negative(num):
    """Check if number is negative"""
    return num < 0

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_zero():
    assert add(2, 0) == 2

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_is_negative():
    assert is_negative(-5) == True
    assert not is_negative(5)

# __init__.py to make the package discoverable as a module
