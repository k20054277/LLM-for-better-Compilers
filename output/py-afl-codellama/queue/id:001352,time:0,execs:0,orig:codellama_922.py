import pytest

def test_and():
    assert 2 and True == 2
    assert 0 and True == 0
    assert 1 and True == 1
    assert 0 and False == 0
    assert 1 and False == 0
    assert 2 and False ==