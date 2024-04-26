
# This Python program demonstrates the use of and and any

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Check if all numbers in the list are greater than 2 using and
if all(number > 2 for number in numbers):
    print("All numbers in the list are greater than 2")

# Check if any number in the list is even using any
if any(number % 2 == 0 for number in numbers):
    print("There is an even number in the list")
