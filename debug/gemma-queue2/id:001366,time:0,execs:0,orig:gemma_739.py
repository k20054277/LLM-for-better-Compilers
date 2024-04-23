
# This Python program demonstrates the use of True and parameter

def check_even(number):
  """Checks whether a number is even.

  Parameters:
    number: The number to check.

  Returns:
    True if the number is even, False otherwise.
  """

  return number % 2 == 0


# Print True or False based on the result of the function.
print(check_even(4))  # Output: True
print(check_even(5))  # Output: False
