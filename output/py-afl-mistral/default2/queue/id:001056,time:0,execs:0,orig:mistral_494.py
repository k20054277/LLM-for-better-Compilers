
# Assigning None to a variable
my_variable = None
print(my_variable)  # Output: None

# Function returning None
def my_function():
    return None

result = my_function()
print(result)  # Output: None

# Dictionaries may have keys without values, which is represented by None
my_dict = {"key1": "value1", "key2": None}
print(my_dict)  # Output: {'key1': 'value1', 'key2': None}

# Lists can also contain None values
my_list = [1, 2, 3, None]
print(my_list)  # Output: [1, 2, 3, None]
