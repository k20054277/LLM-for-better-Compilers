
# A simple function that calculates the square root of a number
def sqrt(number):
    try:
        result = number ** 0.5
    except Exception:
        print("Error: The given number is not a valid number to calculate its square root.")
        return None
    else:
        return result

# Function that tests the square root function with some inputs
def test_sqrt():
    # Test case 1: positive number
    assert sqrt(9) == 3, "Test case 1 failed: The square root of 9 should be 3, not {}.".format(sqrt(9))

    # Test case 2: non-positive number
    assert sqrt(-1) is None, "Test case 2 failed: The square root of -1 should be None, but got {}.".format(sqrt(-1))

    # Test case 3: zero
    assert sqrt(0) == 0, "Test case 3 failed: The square root of 0 should be 0, not {}.".format(sqrt(0))

    print("All tests passed!")

# Run the test function
test_sqrt()

# A wrong input to demonstrate the use of assert with False
number = "hello"
assert sqrt(number) is not None, "The given number '{}' should not have a square root value.".format(number)
