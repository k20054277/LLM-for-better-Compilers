
# Create two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Assign list2 to list1 using 'as' keyword
list1 as list2
# This line will raise a SyntaxError since 'as' is not used for assignment in this context

# Use '+' operator to concatenate two lists
concatenated_list = list1 + list2
print("Concatenated List: ", concatenated_list)

# Use '+=', compound assignment operator, to merge two lists into one
list1 += list2
print("List1 after using +=: ", list1)
