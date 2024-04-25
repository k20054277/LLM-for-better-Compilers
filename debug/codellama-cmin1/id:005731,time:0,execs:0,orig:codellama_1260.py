# This program uses the "as" keyword to create an alias for a variable,
# and the "{}" syntax to unpack a dictionary into separate variables.

# Dictionary with key-value pairs
my_dict = {"name": "John", "age": 30}

# Create an alias for the "name" key using "as"
name = my_dict["name"]
print(name) # Output: John

# Unpack the dictionary into separate variables using "{}" syntax
name, age = my_dict.values()
print(age) # Output: