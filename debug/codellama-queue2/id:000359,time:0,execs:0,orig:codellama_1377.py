def my_function(x):
    assert x >= 0, "x must be non-negative"
    return x * 2

def test_my_function():
    # Test that the function returns the correct value for positive inputs
    assert my_function(5) == 10
    # Test that the function raises an error for negative inputs
    with pytest.raises(AssertionError):
        my_function(-5)