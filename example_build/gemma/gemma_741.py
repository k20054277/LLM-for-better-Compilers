
def is_even(num):
  """Checks whether a number is even.

  Args:
    num: The number to check.

  Returns:
    True if num is even, False otherwise.
  """

  return num % 2 == 0


# Print True or False based on the result of is_even(5)
print(is_even(5))  # Output: False

# Print True or False based on the result of is_even(6)
print(is_even(6))  # Output: True
