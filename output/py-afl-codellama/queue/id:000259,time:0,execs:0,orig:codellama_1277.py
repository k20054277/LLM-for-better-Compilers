# Importing the math module
import math

def test_sqrt(x):
    # Using the assert function to check if x is a positive number
    assert x > 0, "x must be a positive number"

    # Using the from function to get the square root of x
    result = math.sqrt(x)

    # Printing the result
    print("The square root of", x, "is", result)

# Testing the test_sqrt function with different inputs
test_sqrt(-1)  # Should raise an AssertionError
test_sqrt(0)   # Should print "The square root of 0 is 0"
test_sqrt(1)   # Should print "The square root of 1 is 1"
test_sqrt(4)   # Should print "The square root of 4 is 2"