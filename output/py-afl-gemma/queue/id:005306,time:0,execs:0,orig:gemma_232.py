
# This Python program demonstrates the use of and and slice operations

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use the and operator to check if all elements in the list are greater than 5
all_greater_than_5 = all(x > 5 for x in numbers)

# Print the result
print(all_greater_than_5)

# Slice the list to get the elements from the beginning to the second element
slice_of_numbers = numbers[:2]

# Print the slice
print(slice_of_numbers)
