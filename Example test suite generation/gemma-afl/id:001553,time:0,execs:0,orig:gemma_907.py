
# This Python program demonstrates the use of the and and range functions

# Define a range of numbers from 1 to 10
numbers = range(1, 11)

# Use the and operator to check if the number is in the range
for num in numbers:
    if num % 2 == 0 and num % 3 == 0:
        print(num)

# Output:
# 6
# 9
