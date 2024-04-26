
import random

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use randrange() to generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Check if the random number is even or odd
if random_number % 2 == 0:
  print("The random number is even")
else:
  print("The random number is odd")
