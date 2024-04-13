
# This Python program demonstrates the use of assert and or

# Define a function to check if a number is even
def is_even(num):
  return num % 2 == 0

# Assert that 4 is even
assert is_even(4)

# Or statement to handle the case where 4 is not even
or is_even(4):
  print("4 is not even")

# Assert that 5 is not even
assert not is_even(5)

# Print a message if the assertions are successful
print("All assertions are successful")
