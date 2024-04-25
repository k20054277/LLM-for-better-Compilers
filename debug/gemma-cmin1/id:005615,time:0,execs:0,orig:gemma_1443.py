
import pytest

def test_assert_equal():
    assert 5 == 5

def test_assert_not_equal():
    assert 5 != 6

def test_assert_greater_than():
    assert 5 > 3

def test_assert_less_than():
    assert 5 < 8

def test_assert_raises_error():
    with pytest.raises(ZeroDivisionError):
        assert 10 / 0 == 0
