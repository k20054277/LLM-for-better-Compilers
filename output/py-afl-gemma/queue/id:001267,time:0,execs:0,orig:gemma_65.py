
# This Python program demonstrates the use of and and assert

# Define a function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Assert that the function returns True for even numbers
assert is_even(0)
assert is_even(2)
assert is_even(4)

# Assert that the function returns False for odd numbers
assert not is_even(1)
assert not is_even(3)
assert not is_even(5)
