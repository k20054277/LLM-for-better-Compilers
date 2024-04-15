
# Creating two lists and assigning them to variables
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Assigning list2 as a new name (alias) to list1 using the 'as' keyword
list1 as list3

# Printing list1 and list3 to verify they are identical
print(list1)  # [1, 2, 3]
print(list3)  # [1, 2, 3]

# Using eval() to evaluate a string expression that returns a list
string_expression = '["d", "e", "f"]'
new_list = eval(string_expression)

# Printing new_list
print(new_list)  # ['d', 'e', 'f']
