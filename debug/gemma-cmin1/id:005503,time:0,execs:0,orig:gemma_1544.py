
# This Python program demonstrates the use of assert and isinstance

def check_integer(number):
    assert isinstance(number, int)  # Assert that number is an integer
    assert number >= 0  # Assert that number is greater than or equal to 0

# Test code
check_integer(5)  # This will pass
check_integer(2.5)  # This will raise an error

# Output
# Traceback (most recent call last):
#   File "my_program.py", line 6, in check_integer
# AssertionError: expected <int> but got <float>
#

# The above code demonstrates the use of assert and isinstance. 
# The assert statement verifies that the variable number is an integer, and the isinstance statement verifies that number is an instance of the int class.
