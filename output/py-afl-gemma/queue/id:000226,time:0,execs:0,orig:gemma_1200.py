
import pytest

def square(x):
    return x ** 2

@pytest.mark.parametrize("x", [1, 2, 3])
def test_square(x):
    assert square(x) == x ** 2
