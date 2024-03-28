
import pytest

def test_false():
    assert False

def test_true():
    assert True

def test_equal():
    assert 10 == 10

def test_not_equal():
    assert 10 != 12

@pytest.mark.parametrize("number", [1, 2, 3])
def test_greater_than(number):
    assert number > 0

def test_raises_error():
    with pytest.raises(ZeroDivisionError):
        assert 10 / 0 == 0
