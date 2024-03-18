
# This Python program demonstrates the use of False and testing

# Define a function to test if a number is even
def is_even(num):
  return num % 2 == 0

# Test if 6 is even
if is_even(6):
  print("6 is even")

# Test if 5 is even
if not is_even(5):
  print("5 is not even")

# Test if False is False
if False:
  print("False is False")

# Test if True is True
if True:
  print("True is True")
