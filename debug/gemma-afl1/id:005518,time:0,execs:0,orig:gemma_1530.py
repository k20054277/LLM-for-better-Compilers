
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

# Test code
assert divide(10, 2) == 5
assert divide(10, 0) raises ZeroDivisionError

print("All tests passed!")
