
# This Python program demonstrates the use of True and or

# Define a function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use True and or to check if the number is even
for num in numbers:
    if is_even(num) or num % 3 == 0:
        print(num)
