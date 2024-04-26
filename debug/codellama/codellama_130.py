my_list = [1, 2, 3, 4, 5]

# Using the and operator to filter out elements that are less than 3
filtered_list = [x for x in my_list if x >= 3]
print(filtered_list)  # Output: [3, 4, 5]

# Slicing to access a subset of the list
sublist = my_list[1:]
print(sublist)  # Output: [2, 3, 4, 5]