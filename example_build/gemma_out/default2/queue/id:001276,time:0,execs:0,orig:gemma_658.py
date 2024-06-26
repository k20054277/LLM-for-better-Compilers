
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use True to filter out even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

# Use map to double each number in the list
doubled_numbers = map(lambda x: x * 2, numbers)

# Print the results
print(even_numbers)
print(doubled_numbers)
