
# This Python program demonstrates the use of True and dependency.

# Define a function that returns True if the input number is even.
def is_even(n):
  return n % 2 == 0

# Define a function that checks if a number is divisible by 3 and returns True if it is.
def is_ divisible_by_3(n):
  return n % 3 == 0

# Create a variable called number and assign it a value.
number = 6

# Check if the number is even and divisible by 3.
if is_even(number) and is_ divisible_by_3(number):
  print("The number", number, "is even and divisible by 3.")
else:
  print("The number", number, "is not even or divisible by 3.")
