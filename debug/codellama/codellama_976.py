# Using "and" with "process" in Python

# Create a list of integers
numbers = [1, 2, 3, 4, 5]

# Use "and" to check if all elements are greater than 0
if all(number > 0 for number in numbers):
    print("All elements are greater than 0")
else:
    print("Not all elements are greater than 0")

# Use "and" with "process" to check if the sum of all elements is divisible by 3
if process(sum(numbers) % 3 == 0):
    print("The sum of all elements is divisible by 3")
else:
    print("The sum of all elements is not divisible by 3")