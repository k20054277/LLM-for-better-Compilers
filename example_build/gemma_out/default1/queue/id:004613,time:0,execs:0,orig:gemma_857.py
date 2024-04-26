
# This Python program demonstrates the use of and and all

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Check if all numbers in the list are greater than 2 using the all function and and operator
if all(number > 2 for number in numbers) and all(number % 2 == 0 for number in numbers):
    print("All numbers in the list are greater than 2 and divisible by 2")

# Output
# All numbers in the list are greater than 2 and divisible by 2
