def test_assert(x):
    assert x > 0, "x must be positive"
    return x ** 2

print(test_assert(-1)) # Output: AssertionError: x must be positive

print(test_assert(1)) # Output: