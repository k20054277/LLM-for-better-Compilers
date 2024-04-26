import random

# generate a random number between 1 and 10
random_number = random.randint(1, 10)

# check if the random number is within a certain range
assert random_number >= 5 and random_number <= 8

print("The random number is:", random_number)