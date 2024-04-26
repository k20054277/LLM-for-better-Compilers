
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use False to filter out even numbers using map
even_numbers = list(map(lambda x: x % 2 == 0, numbers))

# Print the even numbers
print(even_numbers)
