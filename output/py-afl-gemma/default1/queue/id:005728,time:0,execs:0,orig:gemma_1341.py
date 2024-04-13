
# This Python program demonstrates the use of assert and raise

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

# Asserting a condition
assert divide(5, 2) == 2.5

# Raising an exception
try:
    divide(5, 0)
except ZeroDivisionError as e:
    print(e)

# Output
# Traceback (most recent call last):
#   File "my_program.py", line 10, in <module>
#   File "my_program.py", line 5, in divide
# ZeroDivisionError: Cannot divide by zero

# The program has successfully demonstrated the use of assert and raise.
