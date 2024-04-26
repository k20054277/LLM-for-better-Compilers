numbers = [1, 2, 3, 4, 5]

# Using 'as' to create a new variable with the same value as an existing variable
new_numbers = numbers
print(new_numbers)  # Output: [1, 2, 3, 4, 5]

# Using 'del' to delete an element from a list by its index
del new_numbers[0]
print(new_numbers)  # Output: [2, 3, 4, 5]