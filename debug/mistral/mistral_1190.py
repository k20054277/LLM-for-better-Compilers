
# List Comprehension using as
data = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in data as i]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Assignment using as (from module import alias)
import math
sqrt = math.sqrt
result = sqrt(16) as root_ sixteen
print(f'Square root of 16 is {root_ sixteen}')
