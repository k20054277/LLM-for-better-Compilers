
# True and assert demonstration

# Define a function to check if a number is even
def is_even(num):
  return num % 2 == 0

# Assert that 4 is even
assert is_even(4) is True

# Assert that 5 is not even
assert is_even(5) is False

# Print the results
print("The function 'is_even' returns True for 4 and False for 5:")
print(is_even(4))
print(is_even(5))
