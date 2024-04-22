
# This Python program demonstrates the use of assert and <=

def check_number(num):
    assert num >= 0
    assert num <= 10

# Testing the function with different numbers
check_number(5)
check_number(0)
check_number(11)

# Output
# Traceback (most recent call last):
#   File "my_program.py", line 5, in check_number
# AssertionError: expected <= 10, actual is 11
