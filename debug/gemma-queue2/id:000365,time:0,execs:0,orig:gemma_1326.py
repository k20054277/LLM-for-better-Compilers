
# This Python program demonstrates the use of assert and else.

# Define a function to check if a number is even.
def is_even(num):
    # Assert that num is an integer.
    assert isinstance(num, int)

    # If num is divisible by 2, return True.
    else:
        return num % 2 == 0


# Test the function.
is_even(4)  # Output: True
is_even(5)  # Output: False

# If the assert fails, an error message will be printed.
# For example:
# is_even(3)  # Output: Traceback (most recent call last):
#   File "my_program.py", line 7, in is_even
#     assert isinstance(num, int)
# AssertionError: expected <class '__int__'>, got <class 'float'>
