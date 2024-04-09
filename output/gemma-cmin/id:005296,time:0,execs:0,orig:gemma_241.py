
# Demonstrating the use of and and zip

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use and to compare two lists
even_numbers = [x for x in numbers if x % 2 == 0]

# Use zip to iterate over two lists simultaneously
squares = [x**2 for x, y in zip(numbers, even_numbers)]

# Print the results
print(even_numbers)
print(squares)
