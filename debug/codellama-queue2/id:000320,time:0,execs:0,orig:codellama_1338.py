# Test whether a list contains only integers
assert all(isinstance(x, int) for x in my_list), "List contains non-integer elements"

# Slice the first 5 elements of the list
print(my_list[:5])