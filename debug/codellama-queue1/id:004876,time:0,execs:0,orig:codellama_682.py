def test_true():
    # Tests the True value
    assert True == 1
    assert not False == 0

def test_reversed():
    # Tests the reversed function
    assert list(reversed([1, 2, 3])) == [3, 2, 1]