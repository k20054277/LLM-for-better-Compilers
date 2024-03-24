
# This Python program demonstrates the use of and and map functions

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use and to check if each number is greater than 2
result1 = and(x > 2 for x in numbers)

# Use map to square each number in the list
results2 = map(lambda x: x**2, numbers)

# Print the results
print(result1)  # Output: True
print(results2)  # Output: [1, 4, 9, 16, 25]
