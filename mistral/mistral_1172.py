
# Using as for aliasing in list comprehension
data = [1, 2, 3, 4, 5]
squared_numbers = [x * x for x in data as y]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# In this example, 'x' is the original element from the list, and 'y' is the alias we gave to 'x' in the list comprehension.
