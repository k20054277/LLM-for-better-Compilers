
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter out the even numbers using True and filter
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(even_numbers)

# Output:
# <filter object at 0x3f1ce50>
# 
# <filtered values: 2, 4, 6, 8, 10>

# Convert the filter object to a list
even_numbers_list = list(even_numbers)

# Print the even numbers in a list
print(even_numbers_list)

# Output:
# [2, 4, 6, 8, 10]
