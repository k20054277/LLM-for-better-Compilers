
# This Python program demonstrates the use of the and and oct operators

# Define a function to demonstrate the use of the and operator
def and_operator(a, b):
  """Demonstrates the use of the and operator."""

  # Check if a and b are both True
  if a and b:
    print("a and b are both True")

# Define a function to demonstrate the use of the oct operator
def oct_operator(n):
  """Demonstrates the use of the oct operator."""

  # Convert n to an octal string
  oct_string = str(n) + " oct"

  # Print the octal string
  print(oct_string)

# Example usage
and_operator(True, True)
oct_operator(12)
