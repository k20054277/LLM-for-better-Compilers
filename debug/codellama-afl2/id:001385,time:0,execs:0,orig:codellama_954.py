def test_and(x, y):
    assert x > 0 and y > 0, "Both x and y must be positive"
    return x + y

test_and(-1, -2) # This should raise an AssertionError