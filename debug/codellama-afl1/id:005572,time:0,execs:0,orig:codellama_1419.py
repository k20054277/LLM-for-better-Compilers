def test_assert(a, b):
    """Test that a and b are equal."""
    assert a == b, "Values not equal"

def test_refactor(x, y, z):
    """Test that x is less than y, but not less than z."""
    if x < y and x >= z:
        print("x is less than y, but not less than z")
    else:
        print("x is not less than y or z")

# Test the assert function
test_assert(5, 5)
test_assert(5, 6)

# Test the refactoring function
test_refactor(2, 4, 3)
test_refactor(1, 2, 1)