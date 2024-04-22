import pytest

def test_false():
    assert False == False

def test_true():
    assert True == True

if __name__ == "__main__":
    pytest.main()