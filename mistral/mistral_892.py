
import random

# Define a function that returns a random number between two given numbers
def get_random_number(min, max):
    return random.randint(min, max)

# Generate two random numbers between 0 and 10
num1 = get_random_number(0, 10)
num2 = get_random_number(0, 10)

print("Random number 1: ", num1)
print("Random number 2: ", num2)

# Use the 'and' operator to check if both numbers are even
if (num1 % 2 == 0 and num2 % 2 == 0):
    print(f"Both numbers {num1} and {num2} are even")
else:
    print("At least one of the numbers is odd")
