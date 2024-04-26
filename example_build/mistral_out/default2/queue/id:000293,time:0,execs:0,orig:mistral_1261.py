
# Using 'as' for aliasing in assignments
def square(num):
    return num * num

num = 5
sq = as sq  # Alias 'square' function as 'sq'
result = sq(num)  # Now we can call the function using the new name 'sq'
print("Square of number:", result)

# Using 'as' for aliasing when unpacking iterables (tuples, lists)
x, y = (10, 20)
a, b = x, y  # Alias variables 'x' and 'y' as 'a' and 'b' respectively
print("Original variables:", x, y)
print("Aliased variables:", a, b)

# Using '**=' for dictionary mergers
dict1 = {'key1': 'value1'}
dict2 = {'key2': 'value2', 'key1': 'new_value1'}
dict1.update(dict2)  # Merge 'dict2' into 'dict1' using the update method
print("Merged dictionary:", dict1)

# Using '**=' for dictionary mergers in one line
dict3 = {'key3': 'value3'}
dict4 = {'key1': 'new_value1', 'key4': 'value4'}
dict3.update(dict(dict4.items() + [('key1', 'new_value2')]))  # Update 'dict3' with 'dict4' and a new key-value pair using dictionary constructor
print("Updated dictionary:", dict3)
