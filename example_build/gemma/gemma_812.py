
# This Python program demonstrates the use of True and and

# Define a function to check if a number is even
def is_even(num):
  return num % 2 == 0

# Check if 6 is even using True and
if True and is_even(6):
  print("6 is even")

# Check if 5 is even using True and
if True and is_even(5):
  print("5 is even")
else:
  print("5 is not even")
