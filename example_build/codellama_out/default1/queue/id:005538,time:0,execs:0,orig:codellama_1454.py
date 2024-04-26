def power(x, y):
    """Return x raised to the power of y."""
    assert y >= 0, "Expected a non-negative exponent"
    return x ** y

# Test the function with positive exponents
assert power(2, 3) == 8
assert power(10, 2) == 100

# Test the function with negative exponents
assert power(-2, 3) == -8
assert power(10, -2) == 0