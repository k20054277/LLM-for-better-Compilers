
def add(x, y):
    assert x is not None, "First argument cannot be None"
    assert y is not None, "Second argument cannot be None"
    return x + y

try:
    add(3, 4)
except AssertionError as e:
    print("Error:", e)

# Output: No error because the arguments are valid

try:
    add(None, 5)
except AssertionError as e:
    print("Error:", e)

# Output: Error: First argument cannot be None
