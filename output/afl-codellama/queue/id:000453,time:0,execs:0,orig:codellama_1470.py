# Example using assert and <>

def test_assert(x, y):
    assert x > 0 and y < 10
    return x + y

def test_not_equal(x, y):
    if x != y:
        print("x is not equal to y")
    else:
        print("x is equal to y")

# Testing the function using assert and <>

x = 10
y = 20
assert test_assert(x, y) == 30
print("<", x, ">", "<", y, ">")
test_not_equal(x, y)