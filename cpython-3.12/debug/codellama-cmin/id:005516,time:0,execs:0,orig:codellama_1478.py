numbers = [1, 2, 3, 4, 5]
assert len(numbers) > 0

# Unpack the list using ellipses
first_number, *remaining_numbers = numbers

print(first_number)    # Output: 1
print(remaining_numbers)   # Output: [2, 3, 4, 5]