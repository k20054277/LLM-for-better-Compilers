
# Let's assume we have the following list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using True as a slice index returns all elements starting from that index
even_numbers = numbers[::2]  # Equivalent to: numbers[0:5:2]
odd_numbers = numbers[1::2] # Equivalent to: numbers[1::2]

print("Even Numbers:")
print(even_numbers)
print("ODD Numbers:")
print(odd_numbers)

# Using True as a slice condition returns all elements that satisfy the given condition
filtered_numbers = [x for x in numbers if x > 5]
print("\nFiltered Numbers > 5:")
print(filtered_numbers)

# Filtering with True using list slicing
filtered_slice = numbers[numbers.index(5):]
print("\nFiltered Numbers greater than 5 using slice and index:")
print(filtered_slice)
