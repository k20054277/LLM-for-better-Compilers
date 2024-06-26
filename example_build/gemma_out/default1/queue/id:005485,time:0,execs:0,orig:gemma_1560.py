
# This Python program demonstrates the use of assert and {}

def check_even(number):
    assert number % 2 == 0
    print(f"The number {number} is even.")

# This code will pass
check_even(4)

# This code will fail
check_even(5)

# The output of the program
# The number 4 is even.
# Traceback (most recent call last):
#   File "example.py", line 4, in check_even
# AssertionError: number % 2 != 0
