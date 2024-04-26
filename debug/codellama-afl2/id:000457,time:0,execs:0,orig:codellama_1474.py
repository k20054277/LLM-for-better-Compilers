def test_condition(x):
    assert x > 0, "x must be greater than 0"
    if not x % 2 == 0:
        return True
    else:
        return False

print(test_condition(5)) # Should print True
print(test_condition(-1)) # Should raise an AssertionError