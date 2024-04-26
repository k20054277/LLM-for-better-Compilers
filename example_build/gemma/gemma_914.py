
# Python program to demonstrate the use of and and sorted

# Create a list of numbers
numbers = [1, 3, 5, 2, 4, 6]

# Use the and operator to filter out even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

# Sort the even numbers in ascending order
even_numbers.sort()

# Print the sorted even numbers
print(even_numbers)
