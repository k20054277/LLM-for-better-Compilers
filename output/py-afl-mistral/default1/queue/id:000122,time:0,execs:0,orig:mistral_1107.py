
# Given list of numbers
numbers = [5, 2, 8, 1, 9, 4]

# Using min function with a key function as an argument
min_value = min(numbers, key=lambda x: x)

print("Minimum value in the given list is:", min_value)

# Using as keyword for aliasing a list slice
subset_as = numbers[0:3]  # First three elements of the list 'numbers'
print("\nSubset of first three elements: ", subset_as)

print("Minimum value in the subset is:", min(subset_as))
