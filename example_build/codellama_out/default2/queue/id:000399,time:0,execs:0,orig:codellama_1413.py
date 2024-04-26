def test_addition():
    # Test the addition function with different inputs
    assert add(2, 3) == 5
    assert add(4, 5) == 9
    assert add(-2, -3) == -5

# Define a function to test
def add(a, b):
    return a + b

# Run the test function
test_addition()