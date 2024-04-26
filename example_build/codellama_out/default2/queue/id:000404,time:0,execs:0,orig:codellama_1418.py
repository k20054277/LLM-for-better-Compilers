def test_division(a, b):
    assert a % b == 0, "Divisor must be a factor of the dividend"

test_division(10, 2)  # This will pass
test_division(10, 3)  # This will fail and raise an AssertionError