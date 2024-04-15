
# Original list
numbers = [1, 2, 3, 4, 5]

# Aliasing using as keyword
squared_numbers as nums => [x**2 for x in numbers]

print(nums)  # Output: [1, 4, 9, 16, 25]
