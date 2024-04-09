
# This Python program demonstrates the use of and and assertion

# Define a function called is_even
def is_even(num):
  return num % 2 == 0

# Assert that the function returns True if the input number is even
assert is_even(0)
assert is_even(2)
assert is_even(4)

# Assert that the function returns False if the input number is not even
assert not is_even(1)
assert not is_even(3)
assert not is_even(5)

# Print a message to the console
print("All assertions are true!")
