
# This Python program demonstrates the use of True and return

def check_even(num):
  """Checks whether a number is even.

  Args:
    num: The number to check.

  Returns:
    True if num is even, False otherwise.
  """

  return num % 2 == 0


# Check if 6 is even
even_6 = check_even(6)

# Print the result
print(even_6)  # Output: True
