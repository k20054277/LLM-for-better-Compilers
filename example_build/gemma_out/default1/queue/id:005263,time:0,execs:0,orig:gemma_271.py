
import pytest

def and_function(a, b):
    return a and b


@pytest.mark.parametrize("a, b", [(True, True), (True, False), (False, False)])
def test_and_function(a, b):
    assert and_function(a, b) is True


def test_and_function_with_exception():
    with pytest.raises(ZeroDivisionError):
        and_function(10, 0)
