
# This Python program demonstrates the use of and and len

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Check if all numbers in the list are greater than 2 and the length of the list is greater than 3
if all(num > 2 for num in numbers) and len(numbers) > 3:
  print("All numbers in the list are greater than 2 and the length of the list is greater than 3")

# Output
# All numbers in the list are greater than 2 and the length of the list is greater than 3
