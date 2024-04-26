
import pytest

def my_function(x, y):
    return x + y

def test_my_function():
    assert my_function(2, 3) == 5
    assert my_function(4, 5) == 9

    with pytest.raises(TypeError):
        my_function("a", "b")
