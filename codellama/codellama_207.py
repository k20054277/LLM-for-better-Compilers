# Using False and filter() to remove all even numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(filtered_numbers) # Output: [1, 3, 5, 7, 9]