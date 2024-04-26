import pytest

def test_true():
    assert True == True

def test_false():
    assert False == False

def test_not_equal():
    assert 1 != 2

if __name__ == "__main__":
    pytest.main()