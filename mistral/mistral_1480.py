
def add(x, y):
    assert x is not None and y is not None, "Both x and y must be provided"
    return x + y

try:
    result = add(3, 5)
except AssertionError as e:
    print(e)
else:
    print("Result:", result)
