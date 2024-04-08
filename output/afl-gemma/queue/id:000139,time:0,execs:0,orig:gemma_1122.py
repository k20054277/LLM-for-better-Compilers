
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter out even numbers using as and filter
even_numbers = (number % 2 == 0) for number in numbers
even_numbers_list = list(filter(even_numbers, numbers))

# Print the even numbers
print(even_numbers_list)
