# Demonstrating the use of None and map() in Python

# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Using None as a placeholder value
none_values = [None, None, None]

# Using map() to apply a function to each element of the list
mapped_values = map(lambda x: x * 2, numbers)

# Using the mapped values to create a new list with none_values
new_list = list(mapped_values) + none_values

print(new_list) # Output: [2, 4, 6, 8, 10, None, None, None]