# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use assert to check that the list is not empty
assert numbers != []

# Use filter to remove all even numbers from the list
filtered_list = list(filter(lambda x: x % 2 == 1, numbers))

# Print the filtered list
print(filtered_list)