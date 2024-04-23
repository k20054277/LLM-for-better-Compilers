# This program demonstrates the use of "and" and "pytest"

def test_true():
    assert True and True == True
    assert False and True == False
    assert True and False == False

def test_false():
    assert False and False == False
    assert True and True == True
    assert False and True == False

if __name__ == '__main__':
    import pytest
    pytest.main(["-k", "test_true"])