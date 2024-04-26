
# List with some None values
numbers = [1, 2, None, 4, 5, None, 7]

# Using any() to check if there is a non-zero number in the list
has_non_zero = any(number is not None and number for number in numbers)
print("Has non-zero number:", has_non_zero)

# List with only None values
empty_list = [None, None, None]

# Using any() to check if an empty list with None values has a truthy value
has_truthy = any(empty_list)
print("Has truthy value in empty list:", has_truthy)
