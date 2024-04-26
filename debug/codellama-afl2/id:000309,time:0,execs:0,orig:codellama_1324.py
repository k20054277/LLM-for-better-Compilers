# This program demonstrates the use of assert and oct in Python

# Oct is used to convert an integer to an octal string
assert oct(3) == '0o11'

# Assert can be used to check if a condition is true
assert 2 + 2 == 4, "This should be true"

# If the condition is not true, an AssertionError will be raised
try:
    assert 2 + 2 == 3, "This should be false"
except AssertionError as e:
    print(e)