
# Example of assert statement usage
def square_root(number):
    """Calculates the square root of a given number."""
    assert number >= 0, "Number must be non-negative"
    return number ** 0.5

try:
    result = square_root(-1)
except AssertionError as e:
    print(e)
else:
    print("The square root of {} is {}".format(16, result))
