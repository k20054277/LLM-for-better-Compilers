
# This Python program demonstrates the use of and and max

# Define a list of numbers
numbers = [10, 20, 30, 40, 50]

# Use the and operator to check if all numbers are greater than 20
if all(number > 20 for number in numbers):
    print("All numbers are greater than 20")

# Find the maximum value in the list
max_value = max(numbers)

# Print the maximum value
print("The maximum value in the list is:", max_value)
