
# This Python program demonstrates the use of and and len

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Check if all numbers in the list are greater than 2 using and
if all(num > 2 for num in numbers):
  print("All numbers in the list are greater than 2")

# Get the length of the list using len
length = len(numbers)

# Print the length of the list
print("The length of the list is:", length)
