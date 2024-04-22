
def square_root(number):
    assert number >= 0, "Error: The number must be non-negative"
    return number ** 0.5

try:
    print(square_root(-1))
except AssertionError as e:
    print(e)
