def add(a, b):
    """Adds two numbers together"""
    assert a >= 0 and b >= 0, "Positive integers only!"
    return a + b

print(add(-1, 2)) # Output: AssertionError: Positive integers only!