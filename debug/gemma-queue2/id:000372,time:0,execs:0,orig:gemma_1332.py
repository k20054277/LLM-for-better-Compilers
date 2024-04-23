
# Define a function to check if a number is even
def is_even(num):
  return num % 2 == 0

# Assert that the function returns True for even numbers
assert is_even(0)
assert is_even(2)

# Assert that the function returns False for odd numbers
assert not is_even(1)
assert not is_even(3)

# If the function returns False, print an error message
if not is_even(5):
  print("Error: 5 is not even")

# Otherwise, print a message indicating that the function is working correctly
else:
  print("The function is working correctly")
