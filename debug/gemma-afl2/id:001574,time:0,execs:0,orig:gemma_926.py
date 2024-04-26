
import random

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use randrange() to generate a random number between 0 and the length of the numbers list
random_index = random.randrange(0, len(numbers))

# Print the number at the random index
print(numbers[random_index])
