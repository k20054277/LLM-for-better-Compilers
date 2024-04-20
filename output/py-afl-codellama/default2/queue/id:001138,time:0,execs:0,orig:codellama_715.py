import pytest

def test_true():
    assert True == True

@pytest.mark.parametrize("value", [1, 2, 3])
def test_true_for_values(value):
    assert value >