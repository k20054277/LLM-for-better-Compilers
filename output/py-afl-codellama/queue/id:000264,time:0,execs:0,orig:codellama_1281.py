def test_assert(x):
    assert x > 0, "x must be positive"
    return x * x

# Test the function with a positive value
print(test_assert(5)) # Output: 25

# Test the function with a negative value
try:
    print(test_assert(-5))
except AssertionError as e:
    print("AssertionError:", e) # Output: AssertionError: x must be positive