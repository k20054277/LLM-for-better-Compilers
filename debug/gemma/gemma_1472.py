
# This Python program demonstrates the use of assert and statement

def check_even(number):
    """Checks whether a given number is even."""
    if number % 2 == 0:
        return True
    else:
        return False

# Asserting that the function returns True for even numbers
assert check_even(0) is True
assert check_even(2) is True
assert check_even(4) is True

# Asserting that the function returns False for odd numbers
assert check_even(1) is False
assert check_even(3) is False
assert check_even(5) is False

# Printing a statement
print("All assertions are successful!")
