
# This Python program demonstrates the use of assert and zip

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Assert that the sum of the numbers in the list is equal to 16
assert sum(numbers) == 16

# Zip the numbers in the list with their squares
squares = zip(numbers, [x**2 for x in numbers])

# Print the squares
print(squares)
