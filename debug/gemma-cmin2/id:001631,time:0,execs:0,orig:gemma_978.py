
def divisible_by_three(number):
  """Checks if a number is divisible by three.

  Args:
    number: The number to check.

  Returns:
    True if the number is divisible by three, False otherwise.
  """

  return number % 3 == 0


# Test code
print(divisible_by_three(6))  # Output: True
print(divisible_by_three(9))  # Output: True
print(divisible_by_three(15))  # Output: True
print(divisible_by_three(12))  # Output: False
