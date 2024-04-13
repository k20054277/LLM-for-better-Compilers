def demonstrate_none(x):
    if x is not None:
        assert x > 0, "x must be positive"
    return x

# Test the function with different inputs
print(demonstrate_none(-1)) # Output: AssertionError: x must be positive
print(demonstrate_none(0)) # Output: None
print(demonstrate_none(1)) # Output: