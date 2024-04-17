# Using 'and' with 'map' to filter a list of numbers
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
filtered_numbers = map(is_even, numbers)
print(list(filtered_numbers)) # Output: [2, 4, 6]