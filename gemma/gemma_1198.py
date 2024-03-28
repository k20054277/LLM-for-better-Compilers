
import pytest

def my_function(x):
    return x * 2

@pytest.mark.parametrize("x", [1, 2, 3])
def test_my_function(x):
    assert my_function(x) == x * 2

def test_my_function_with_error(x):
    with pytest.raises(ZeroDivisionError):
        my_function(x) / 0
