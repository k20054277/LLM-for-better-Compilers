
# File: test_addition.py
def test_add():
    # Test case for addition of two positive numbers
    assert add(2) + add(3) == add(5), "Addition of two positive numbers is not correct"
    
    # Test case for addition of a negative and positive number
    assert add(-1) + add(2) == add(0), "Addition of a negative number and positive number is not correct"

def test_add_zero():
    # Test case for addition of a number with zero
    assert add(3) + 0 == add(3), "Addition of a number with zero is not correct"
    
def test_add_large_numbers():
    # Test case for addition of large numbers
    assert add(12345) + add(67890) == add(80235), "Addition of large numbers is not correct"
