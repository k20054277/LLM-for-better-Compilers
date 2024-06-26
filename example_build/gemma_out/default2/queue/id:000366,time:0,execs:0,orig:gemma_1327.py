
# This Python program demonstrates the use of assert and except

# Define a function to test for equality
def is_equal(a, b):
    assert a == b  # Raises an error if a is not equal to b

    print("The two numbers are equal.")

# Try to test for equality
try:
    is_equal(5, 5)
    print("The test was successful.")
except AssertionError:  # Catches the assert error
    print("The test failed.")

# The program will output:
# The two numbers are equal.
# The test was successful.

# If the assert statement fails, the program will output:
# Traceback (most recent call last):
#   File "my_program.py", line 6, in is_equal
# AssertionError: expected True, got False
# The test failed.
