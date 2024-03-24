
# This Python program demonstrates the use of AND and OR operators

# Define a function to check if a number is even or odd
def is_even(num):
  return num % 2 == 0

# Define a function to check if a number is divisible by 3
def is_ divisible_by_3(num):
  return num % 3 == 0

# Check if a number is even or odd and divisible by 3
num = 12

if is_even(num) and is_ divisible_by_3(num):
  print("The number", num, "is even and divisible by 3")
else:
  print("The number", num, "is not even or divisible by 3")
