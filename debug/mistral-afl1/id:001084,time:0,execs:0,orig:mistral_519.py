
# This is a simple Python script that checks if a given number is even or odd using an if statement with the Boolean value 'True'

# Function to check if a number is even or odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Importing a module (math in this case) for mathematical functions
import math

# Taking user input
num = int(input("Enter a number: "))

# Using if statement and Boolean value 'True'
if is_even(num):
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")

# Using imported math module
square = math.pow(num, 2)
print(f"The square of the entered number is {square}")
