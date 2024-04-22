def test_divmod():
    # Testing the divmod function
    result = divmod(10, 3)
    assert result == (3, 1), "The result of divmod(10, 3) is not (3, 1)"

    # Testing with a negative number
    result = divmod(-10, 3)
    assert result == (-3, -1), "The result of divmod(-10, 3) is not (-3, -1)"

# Test the divmod function with different inputs
test_divmod()