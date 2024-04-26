
# This Python program demonstrates the use of and and while.

# Define a function to check if a number is even.
def is_even(n):
  return n % 2 == 0

# Initialize a variable to track the number of even numbers.
even_count = 0

# While the number of even numbers is less than 10, continue looping.
while even_count < 10:
  # Get a number from the user.
  number = int(input("Enter a number: "))

  # Check if the number is even.
  if is_even(number):
    # Increment the number of even numbers.
    even_count += 1

  # Print the number of even numbers.
  print("The number of even numbers is:", even_count)
