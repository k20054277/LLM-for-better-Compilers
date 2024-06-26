# Importing the necessary modules
import random
from math import sqrt

# Defining the function to calculate the square root of a number
def calculate_square_root(number):
    return sqrt(number)

# Creating a list of numbers to calculate their square roots
numbers = [1, 2, 3, 4, 5]

# Using None as a default value for the function's argument
for number in numbers:
    print("The square root of", number, "is", calculate_square_root(number))

# Printing the result with None as the default value
print("The square root of 6 is", calculate_square_root(None))