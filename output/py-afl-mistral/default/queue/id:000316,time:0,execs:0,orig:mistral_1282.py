
def square_root(number):
    """Calculates the square root of a number."""
    assert number >= 0, "Number must be non-negative"
    return number ** 0.5

try:
    print(square_root(-3))
except AssertionError as e:
    print(e)
