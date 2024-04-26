a = ['hello', 'world']
b = ['goodbye', 'cruel', 'world']

print(a[1])  # prints "world"
print(b[0])  # prints "goodbye"

# using "as" to create a new list with the same elements as another list
new_list = a.copy()
print(new_list)  # prints ["hello", "world"]

# using ".." to slice a list and get a new list with specific elements
sub_list = b[1:3]
print(sub_list)  # prints ["cruel", "world"]