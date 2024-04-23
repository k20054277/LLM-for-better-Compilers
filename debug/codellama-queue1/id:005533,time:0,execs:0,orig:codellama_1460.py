def test_less_than_or_equal(a, b):
    assert a <= b

test_less_than_or_equal(10, 20) # This should pass
test_less_than_or_equal(10, 10) # This should also pass
test_less_than_or_equal(20, 10) # This should fail