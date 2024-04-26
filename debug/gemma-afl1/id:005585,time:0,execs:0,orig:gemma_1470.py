
# This Python program demonstrates the use of assert and conditional statements

# Define a function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Assert that the function returns True for even numbers
assert is_even(4)
assert is_even(6)

# Assert that the function returns False for odd numbers
assert not is_even(5)
assert not is_even(7)

# Conditional statement to check if a number is even
if is_even(8):
    print("8 is even")

# Conditional statement to check if a number is odd
if not is_even(9):
    print("9 is odd")
