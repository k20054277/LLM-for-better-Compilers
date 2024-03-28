
# Define a function with incorrect semantics (subtraction instead of addition)
def add(a, b):
    return a - b

def test_add():
    # Test case 1: check addition of two positive numbers
    assert add(3, 2) == 5, "Error: Adding two positive numbers did not give the correct result."

    # Test case 2: check addition of a negative number and a positive number
    assert add(-2, 3) == 1, "Error: Adding a negative number and a positive number did not give the correct result."

    # Test case 3: check addition of zero with any number
    assert add(5, 0) == 5, "Error: Adding a number with zero did not give the expected result."

if __name__ == "__main__":
    test_add()
