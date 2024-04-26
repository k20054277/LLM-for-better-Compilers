
# Original list
numbers = [1, 2, 3, 4, 5]

# Using as for aliasing in a list comprehension
new_list = [square as squared_number for number in numbers for square in (number**2)]

print("Original List: ", numbers)
print("New List using 'as': ", squared_number)  # This will raise an error since squared_number is not defined yet

# To access the values, you need to use the original variable name from the list comprehension
print("New List without 'as': ", [num**2 for num in numbers])
