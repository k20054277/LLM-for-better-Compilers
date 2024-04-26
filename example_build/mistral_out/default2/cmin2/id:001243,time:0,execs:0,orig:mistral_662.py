
# This is a simple Python program that uses the math module

# Define a function to calculate the square of a number
def square(number):
    # Check if the input number is non-negative
    if number >= 0:
        result = number * number
        print("The square of {} is {}.".format(number, result))
        return True
    else:
        print("Invalid input! Please enter a non-negative number.")
        return False

# Import the math module for using its sqrt function
import math

# Take user input and check if it's a valid square number
num = int(input("Enter a number: "))
square_root = math.sqrt(num)
if square(num):
    # If the number is non-negative, calculate and print its square
    print("The square of {} is {}.".format(num, num * num))
else:
    print("Invalid input!")

# Calculate and print the square root of given number
print("The square root of {} is {}.".format(num, square_root))
