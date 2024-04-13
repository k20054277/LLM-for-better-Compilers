
# This Python program demonstrates the use of assert and ;

def my_function(x):
    assert x >= 5
    print(x)

my_function(6)
# Output: 6

my_function(2)
# Output: Traceback (most recent call last):
#   File "my_program.py", line 5, in my_function
# AssertionError: x must be greater than or equal to 5
