
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the and operator to check if each number is greater than 2
is_greater_than_2 = lambda x: x > 2

# Use the map function to apply the is_greater_than_2 function to each number in the numbers list
greater_than_2 = map(is_greater_than_2, numbers)

# Print the results
print(greater_than_2)
