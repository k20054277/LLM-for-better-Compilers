
def divisible_by_three(n):
  """Checks if a number is divisible by 3.

  Args:
    n: The number to check.

  Returns:
    True if n is divisible by 3, False otherwise.
  """

  assert n >= 0
  assert n % 3 == 0
  return True

# Demonstrate the use of assert and next
next_number = divisible_by_three(9)
print(next_number)  # Output: True

# Try to assert a number that is not divisible by 3
assert divisible_by_three(5) is False
