# Use assert to check if a variable has a specific value
x = 5
y = "hello"
assert x == 5, "x should be equal to 5"
assert y == "hello", "y should be equal to 'hello'"

# Use dir to get the list of attributes of an object
my_list = [1, 2, 3]
print(dir(my_list)) # Output: ['append', 'count', 'copy', 'pop', ...]