# Example using assert

def test_assert(x, y):
    assert x == y, "The two numbers are not equal"

test_assert(5, 6)

# Output: AssertionError: The two numbers are not equal

# Example using is

def test_is(x, y):
    if x is y:
        print("x and y are the same object")
    else:
        print("x and y are different objects")

test_is(5, 6)

# Output: x and y are different objects