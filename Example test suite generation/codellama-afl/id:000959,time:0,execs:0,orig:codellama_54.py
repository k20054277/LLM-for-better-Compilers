# This program demonstrates the use of and and del in Python

# Create a dictionary with 5 key-value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Use and to create a new dictionary with only the keys that are less than 3
new_dict = {key: value for key, value in my_dict.items() if key < 3}
print(new_dict) # Output: {'a': 1, 'b': 2}

# Use del to remove the key-value pair with key 'c' from the dictionary
del new_dict['c']
print(new_dict) # Output: {'a': 1, 'b': 2}