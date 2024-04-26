
# This Python program demonstrates the use of True and conditional statements.

# Define a function to check if a number is even.
def is_even(num):
  return num % 2 == 0

# Create a variable to store the number.
number = 10

# Check if the number is even using a conditional statement.
if is_even(number):
  print("The number", number, "is even.")
else:
  print("The number", number, "is not even.")

# Check if the number is even using a True statement.
if True and number % 2 == 0:
  print("The number", number, "is even.")
