import pytest

def double(x):
    return x * 2

def test_double():
    assert double(5) == 10

if __name__ == '__main__':
    pytest.main()