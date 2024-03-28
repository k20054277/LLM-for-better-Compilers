
def check_conditions(arg1, arg2):
  """
  This function checks if two given numbers are positive and even.
  """

  # Checking if the first argument is positive and even
  if isinstance(arg1, int) and arg1 > 0 and arg1 % 2 == 0:
    print(f"The first argument {arg1} is a positive even number.")
  else:
    print(f"The first argument {arg1} does not meet the conditions.")

  # Checking if the second argument is positive and even as well
  if isinstance(arg2, int) and arg2 > 0 and arg2 % 2 == 0:
    print(f"The second argument {arg2} is a positive even number.")
  else:
    print(f"The second argument {arg2} does not meet the conditions.")

# Testing the function with some arguments
check_conditions(3, 5) # Output: The first argument 3 does not meet the conditions. The second argument 5 does not meet the conditions.
check_conditions(6, 8) # Output: The first argument 6 is a positive even number. The second argument 8 is a positive even number.
