
# Using as for aliasing a value from a dictionary
data = {'name': 'John Doe', 'age': 30}
name, age = data.items()[:2] # Extract name and age as separate variables
name_alias = next(item[0] for item in data.items() if item[0] == 'name')[0]
name, _ = (name_alias, age) # Alias 'name' with a shorter variable name
print('Name:', name)

# Using [] for slicing and accessing elements in a list
numbers = [1, 2, 3, 4, 5]
first, second = numbers[0:2] # Extract first two elements as separate variables
print('First two elements:', first, second)

# Using [] for indexing or accessing specific element in a list/string
last_element = numbers[-1] # Get the last element of the list
print('Last element:', last_element)

# Using as to simplify an iterable unpacking assignment when multiple variables have the same name
x, y, x = [1, 2, 3] # SyntaxError
x, (y, x) = [1, (2, 3)] # Valid
print('Variables:', x, y, x)
