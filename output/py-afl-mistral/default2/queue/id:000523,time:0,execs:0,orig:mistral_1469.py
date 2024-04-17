
# my_package/math_ops.py
def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def test_math_ops():
    """Tests for mathematical operations."""
    assert add(3, 5) == 8, "Addition is not working"
    assert subtract(10, 4) == 6, "Subtraction is not working"
    assert multiply(2, 4) == 8, "Multiplication is not working"
    assert divide(10, 2) == 5.0, "Division is not working"
