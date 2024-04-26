# Import the random module to generate random numbers
import random

# Define a function that returns a random number between 1 and 10
def get_random_number():
    return random.randint(1, 10)

# Use the function to get a random number
num = get_random_number()

# Print the number to the console
print("Random number:", num)

# Check if the number is even or odd
if num % 2 == 0:
    print("Even")
else:
    print("Odd")