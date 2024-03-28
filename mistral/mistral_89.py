
# A list to demonstrate with
my_list = [1, 2, 3, 4, 5]

# Using False as a value
if not my_list:
    print("The list is empty")
else:
    print("The list has some elements")
    
# Using reversed() function
print("Original list:", my_list)
my_reverse_iter = reversed(my_list)

# Using False with an iterator (reversed list)
if not next(my_reverse_iter, False):
    print("The reversed list is empty")
else:
    print("First element of the reversed list:", next(my_reverse_iter))

print("Reversed list:")
for i in reversed(my_list):
    print(i)
