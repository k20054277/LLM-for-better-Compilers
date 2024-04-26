
# Assignment using '=' and 'as'
a = 10
b = a
print("Variable 'a' is:", a)
print("Variable 'b' is:", b)
print("ID of variable 'a':", id(a))
print("ID of variable 'b':", id(b))

# Assignment using 'as' with an iterable (like list or tuple)
list_numbers = [1, 2, 3, 4, 5]
new_list = list_numbers
print("Variable 'list_numbers' is: ", list_numbers)
print("Variable 'new_list' is: ", new_list)
print("ID of 'list_numbers':", id(list_numbers))
print("ID of 'new_list':", id(new_list))
print()

# Assignment using 'as' and 'is' with the same object (creates an alias, but IDs are the same)
x = y = [1, 2, 3]
print("Variable 'x' is: ", x)
print("Variable 'y' is: ", y)
print("ID of 'x':", id(x))
print("ID of 'y':", id(y))
print("Are they the same object? ", x is y) # This will return True
