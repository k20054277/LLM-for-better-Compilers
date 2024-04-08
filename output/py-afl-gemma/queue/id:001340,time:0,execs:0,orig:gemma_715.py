
import pytest

def test_true():
    assert True is True

def test_false():
    assert False is False

def test_raises_error():
    with pytest.raises(ZeroDivisionError):
        assert 10 / 0 == 0
