
# Define some variables
num = 10
my_list = [1, 2, 3, 4, 5]
my_dict = {"name": "John", "age": 25}

# Assign None to a variable
none_var = None

# Check if a variable is assigned or not using 'is' keyword and None
print("num is None?: ", num is None)
print("my_list is None?: ", my_list is None)
print("my_dict is None?: ", my_dict is None)
print("none_var is None?: ", none_var is None)

# Assign value to a variable and check if it's in a list or not using 'in' keyword
print("5 in my_list?: ", 5 in my_list)
print("John in my_dict keys?: ", "name" in my_dict.keys())

# Check if None is in a list
print("None in my_list?: ", None in my_list)  # Raises TypeError: 'NoneType' object is not iterable

# Using list with None as an element
my_list_with_none = [1, 2, 3, None, 5]
print("None in my_list_with_none?: ", None in my_list_with_none)

# Checking if a variable is equal to None using '==' operator
print("num == None?: ", num == None)
