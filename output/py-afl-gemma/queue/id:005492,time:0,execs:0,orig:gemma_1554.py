
# This Python program demonstrates the use of assert and is

# Define a function to test if a number is even
def is_even(num):
    return num % 2 == 0

# Assert that 4 is even
assert is_even(4)

# Assert that 5 is not even
assert not is_even(5)

# Print a message if the tests are successful
print("All tests successful!")
