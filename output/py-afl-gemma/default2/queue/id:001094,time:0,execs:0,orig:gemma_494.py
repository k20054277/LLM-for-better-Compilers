
# Define a function that checks if a number is even
def is_even(num):
  # If the number is None, return False
  if num is None:
    return False

  # If the number is even, return True
  else:
    return num % 2 == 0


# Print the result of is_even(5)
print(is_even(5))  # Output: False

# Print the result of is_even(6)
print(is_even(6))  # Output: True

# Print the result of is_even(None)
print(is_even(None))  # Output: False
