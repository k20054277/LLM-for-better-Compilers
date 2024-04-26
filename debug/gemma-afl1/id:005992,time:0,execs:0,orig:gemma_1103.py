
# Demonstrating the use of as and all

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use as and all to check if all numbers are greater than 2
all_greater_than_2 = all(x > 2 for x in numbers)

# Print the result
print(all_greater_than_2)  # Output: True

# Use as and all to find the maximum value in the list
max_value = max(x for x in numbers)

# Print the result
print(max_value)  # Output: 5
