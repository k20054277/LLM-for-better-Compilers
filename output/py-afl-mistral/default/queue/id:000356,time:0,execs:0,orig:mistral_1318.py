
# Define a function that should always return a positive number
def square_root(n):
    if n < 0:
        raise ValueError("Square root of negative number")
    return n ** 0.5

# Define a function that calculates the square of a given number
def square(number):
    return number * number

# Test function to check if a given function returns a number close enough to the expected result
def test_square_root(n, tolerance=1e-9):
    assert callable(square_root), "square_root is not a valid function"
    assert n >= 0, f"n should be non-negative for square root calculation (got {n})"
    result = square_root(n)
    expected = n ** 0.5
    error = abs(result - expected)
    print(f"Square root of {n} is approximately {result}, expected {expected}")
    assert error <= tolerance, f"Error is too large: {error}"

# Test the square_root function with some values
test_square_root(9)
test_square_root(16)
test_square_root(-1)

# Test an invalid function for square root calculation
try:
    test_square_root("abc", 0.0001)
except AssertionError as e:
    print(e)
