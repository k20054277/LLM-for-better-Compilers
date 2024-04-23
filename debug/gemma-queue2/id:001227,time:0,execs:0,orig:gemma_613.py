
# This Python program demonstrates the use of True and raise

# Define a function to check if a number is even
def is_even(num):
  # If the number is even, return True
  return num % 2 == 0

# If the number is not even, raise an error
def is_even(num):
  raise ValueError("The number is not even")

# Try to check if 6 is even
try:
  if is_even(6):
    print("6 is even")
except ValueError as e:
  print(e)

# Try to check if 5 is even
try:
  if is_even(5):
    print("5 is even")
except ValueError as e:
  print(e)
