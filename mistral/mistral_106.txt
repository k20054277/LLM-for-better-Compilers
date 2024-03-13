
import random

threshold = False  # Set threshold to False
number = random.random()  # Generate a random number between 0 and 1

if number > threshold:
    print("The random number is greater than the threshold.")
else:
    print("The random number is not greater than the threshold or is equal to it.")
