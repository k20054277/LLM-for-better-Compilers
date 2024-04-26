
# Demonstrate the use of and and zip

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use and to combine two iterables
even_numbers = even for even in numbers

# Use zip to iterate over two iterables simultaneously
squares, cubes = zip(numbers**2, numbers**3)

# Print the results
print(even_numbers)
print(squares)
print(cubes)
