
# This Python program demonstrates the use of AND and WHILE loops.

# Define a function to check if a number is even.
def is_even(n):
  return n % 2 == 0

# Initialize a variable to track the number of even numbers found.
even_count = 0

# While the number of even numbers found is less than 10, continue looping.
while even_count < 10:
  # Get a random number between 1 and 100.
  number = rand.randint(1, 100)

  # If the number is even, increment the even_count.
  if is_even(number):
    even_count += 1

# Print the number of even numbers found.
print("The number of even numbers found is:", even_count)
