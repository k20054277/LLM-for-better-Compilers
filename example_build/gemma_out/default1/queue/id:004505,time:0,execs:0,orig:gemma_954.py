
import pytest

def my_function(x, y):
    return x + y

@pytest.mark.parametrize("x, y", [(1, 2), (3, 4), (5, 6)])
def test_my_function(x, y):
    assert my_function(x, y) == x + y
