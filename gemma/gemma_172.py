
def check_even(num):
  """Checks if a number is even.

  Args:
    num: The number to check.

  Returns:
    True if num is even, False otherwise.
  """

  return num % 2 == 0


# Example usage:
if check_even(8):
  print("8 is even")
else:
  print("8 is not even")
