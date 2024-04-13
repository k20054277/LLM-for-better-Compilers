
# This Python program demonstrates the use of assert and [].

def my_function(x):
    assert x > 0
    return x * 2

# This will pass
my_function(5)

# This will fail
my_function(-1)

# The output of the program will be:
# Traceback (most recent call last):
#   File "my_program.py", line 5, in <module>
#   AssertionError: x > 0
# 
# The program execution will stop at the line with the assert statement, and the error message will be displayed.
