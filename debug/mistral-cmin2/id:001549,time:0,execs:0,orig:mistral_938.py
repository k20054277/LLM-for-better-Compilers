
# This program checks if two numbers are within a certain range
def is_in_range(num, lower, upper):
  """
  Returns True if the number is within the given lower and upper limits, otherwise False.
  """
  return num >= lower and num <= upper

# Function to get user input
def get_number():
  """
  Get a valid number from the user.
  """
  while True:
    try:
      num = int(input("Enter a number: "))
      break
    except ValueError:
      print("Invalid input. Please enter an integer.")

# Main program
if __name__ == "__main__":
  lower_limit = 10
  upper_limit = 20

  # Get user input
  num = get_number()

  # Check if the number is within the given range using and operator
  in_range = is_in_range(num, lower_limit, upper_limit)

  print(f"Number {num} is in range [{lower_limit}, {upper_limit}]? "
        f"{('Yes' if in_range else 'No')}")
