
# This Python program demonstrates the use of and and < operators

# Define a function to check if a number is greater than 5 and less than 10
def is_between(num):
  return num > 5 and num < 10

# Check if 7 is between 5 and 10
if is_between(7):
  print("7 is between 5 and 10")

# Check if 12 is between 5 and 10
if is_between(12):
  print("12 is between 5 and 10")

# Output
# 7 is between 5 and 10
# 12 is not between 5 and 10
