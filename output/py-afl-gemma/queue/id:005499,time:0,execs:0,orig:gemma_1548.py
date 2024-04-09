
# This Python program demonstrates the use of assert and <<

def square(x):
    return x ** 2

# Asserting that square(5) is equal to 25
assert square(5) == 25

# Printing the value of square(5)
print(square(5))

# Output:
# 25

# Trying to assert that square(6) is equal to 25
assert square(6) == 25

# This will raise an error
# Output:
# Traceback (most recent call last):
#   File "example.py", line 8, in <module>
# AssertionError: expected 25, got 36
