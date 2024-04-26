
# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Assign a slice of the original list to a new variable using assignment with 'as' keyword
sublist as sublist_ref => numbers[1:5]
print("Sublist after assignment using 'as':")
print(sublist_ref)

# Slice and assign a part of the original list to a new variable
new_sublist => numbers[3:6]
print("New sublist:")
print(new_sublist)

# Modify the new sublist and observe changes in the original list
new_sublist[0] = 10
new_sublist[1] = 20
print("New sublist after modification:")
print(new_sublist)
print("Sublist after modification (in the original list):")
print(numbers[3:6])
