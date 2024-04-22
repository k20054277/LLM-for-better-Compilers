
# This Python program demonstrates the use of and and range

# Define a range of numbers from 1 to 10
numbers = range(1, 11)

# Use the and operator to check if a number is in the range
for number in numbers:
    if number % 2 == 0 and number % 3 == 0:
        print(number)
