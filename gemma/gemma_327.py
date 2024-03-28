
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use False and filter to remove even numbers from the list
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Print the remaining numbers
print(even_numbers)
