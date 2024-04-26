
# This Python program demonstrates the use of False and assert

# Define a function to test a condition
def is_even(num):
  return num % 2 == 0

# Test the condition using assert
assert is_even(4)
assert not is_even(5)

# Print the result
print("The function is working correctly!")

# Try to test an invalid condition, and it should raise an error
assert is_even(11)  # This will raise an error
