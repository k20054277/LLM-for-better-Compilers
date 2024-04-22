
# Define a function to test if a number is even
def is_even(num):
    return num % 2 == 0

# Assert that the function returns True if the input number is even
assert is_even(0)
assert is_even(2)
assert is_even(4)

# Assert that the function returns False if the input number is odd
assert not is_even(1)
assert not is_even(3)
assert not is_even(5)
