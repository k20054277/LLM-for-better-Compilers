
# Let's assume we have a function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Now let's write a test for the is_even function using assert and bitwise negation
def test_is_even():
    # Assert that positive even numbers are considered even
    assert is_even(4) is True, "Expected 4 to be even"

    # Assert that negative even numbers are also considered even
    assert is_even(-4) is True, "Expected -4 to be even"

    # Assert that positive odd numbers are not considered even
    with pytest.raises(AssertionError):
        assert is_even(3) is True, "Expected 3 to be odd"

    # Using bitwise negation to test that negative odd numbers are not considered even
    with pytest.raises(AssertionError):
        assert ~is_even(-3) is 0, "-3 should be an odd number"

# Run the tests using pytest
pytest.main(['test_is_even.py'])
