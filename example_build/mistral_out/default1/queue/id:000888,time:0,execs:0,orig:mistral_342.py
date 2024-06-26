
# Define a list with a None value
my_list = [1, 2, "three", None, 5, 6]

print("Original List:")
print(my_list)

# Assign None to an element in the list
my_list[3] = None

print("\nList after assigning None to element at index 3:")
print(my_list)

# Use slicing to extract sublists
print("\nSublist starting from index 1 and ending before index 4:")
sublist1 = my_list[1:4]
print(sublist1)

print("\nSublist starting from the end, with a step size of 2:")
sublist2 = my_list[-3:None:2]
print(sublist2)
