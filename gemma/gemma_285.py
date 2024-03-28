
# Define a function to check if a number is even
def is_even(num):
  # If the number is divisible by 2, it is even
  return num % 2 == 0

# Create a variable to store the number
number = 10

# Check if the number is even using False and elif
if is_even(number):
  print("The number", number, "is even")
else:
  print("The number", number, "is not even")
