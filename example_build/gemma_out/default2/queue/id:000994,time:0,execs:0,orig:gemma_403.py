
import pytest

def test_false():
    assert False is False

def test_true():
    assert True is True

@pytest.mark.parametrize("condition", [True, False])
def test_condition(condition):
    assert condition is condition
