
import pytest

def test_assert_equal():
    a = 10
    b = 10

    assert a == b

    # The following assert will fail
    # assert a != b

def test_assert_raises():
    def raise_error():
        raise ValueError("This is an error")

    with pytest.raises(ValueError):
        raise_error()

    # The following assert will also fail
    # assert raise_error() is not raising the expected error
    # assert False
