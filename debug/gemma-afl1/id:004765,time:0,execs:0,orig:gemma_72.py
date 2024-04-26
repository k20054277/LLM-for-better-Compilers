
# This Python program demonstrates the use of and and del keywords

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the and keyword to check if all elements in the list are greater than 3
all_greater_than_3 = and(x > 3 for x in numbers)

# Print the result
print(all_greater_than_3)

# Delete the element 2 from the list
del numbers[1]

# Print the updated list
print(numbers)
