
def check_even(num):
  """Checks whether a number is even.

  Args:
    num: The number to check.

  Returns:
    True if num is even, False otherwise.
  """

  return num % 2 == 0


# Test code
print(check_even(8))  # Output: True
print(check_even(9))  # Output: False
