
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using as to alias a variable
series_sum as total_sum
total_sum = sum(numbers)

print("Sum of the given list using sum() function and 'as' keyword: ", total_sum)

# Without using 'as'
another_sum = sum(numbers)

print("Sum of the given list using sum() function without 'as': ", another_sum)
