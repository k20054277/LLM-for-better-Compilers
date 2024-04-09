
# This Python program demonstrates the use of and and all

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Check if all numbers in the list are greater than 2 using the all function and and operator
if all(number > 2 for number in numbers) and numbers:
    print("All numbers in the list are greater than 2")

# Check if the first two numbers in the list are even using the and operator
if numbers[0] % 2 == 0 and numbers[1] % 2 == 0:
    print("The first two numbers in the list are even")
