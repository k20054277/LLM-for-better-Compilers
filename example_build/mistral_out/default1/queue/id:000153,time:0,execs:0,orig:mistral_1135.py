
import random

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use random.choice() to select a random element from the list and assign it to a variable using as keyword
random_number = random.choice(numbers) as rn

print("Randomly selected number: ", rn)

# Generate a random float number between 0 and 1 using random.random() as qr
quarter = random.random() as quarter

print("Randomly generated float number: ", quarter)

# Use random.shuffle() to shuffle the list 'numbers' in-place and assign it back to the same variable using as keyword
random.shuffle(numbers) as shuffled_numbers

print("Shuffled numbers: ", shuffled_numbers)
