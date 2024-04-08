
# This Python program demonstrates the use of assert and is

# Define a function to test
def divisible_by_three(n):
  """Checks if a given number is divisible by 3.

  Args:
    n: The number to check.

  Returns:
    True if n is divisible by 3, False otherwise.
  """

  return n % 3 == 0


# Assert that 6 is divisible by 3
assert divisible_by_three(6) is True

# Assert that 7 is not divisible by 3
assert divisible_by_three(7) is False

# Use is operator to compare with True
assert divisible_by_three(6) is True

# Use is operator to compare with False
assert divisible_by_three(7) is False
