
# False and Hash

# False is a boolean value that evaluates to False in boolean comparisons
print(False)  # Output: False

# Hash is a built-in data type that stores key-value pairs
my_hash = {"name": "John Doe", "age": 30}

# You can access values from a hash using their keys
print(my_hash["name"])  # Output: John Doe

# Hash objects are immutable, meaning you cannot change their contents
my_hash["age"] = 31

# Trying to change a key-value pair will raise an error
# my_hash["address"] = "123 Main St"  # Error: cannot modify dict keys

# Hash objects can be used as dictionaries, allowing you to store and retrieve data based on keys
print(my_hash)  # Output: {'name': 'John Doe', 'age': 31}

# You can also use hash objects to store lists of items
my_hash[" hobbies"] = ["reading", "writing", "music"]

# Accessing items from a list stored in a hash
print(my_hash["hobbies"])  # Output: ['reading', 'writing', 'music']

# Note that hash objects are not ordered like lists, so the items may not be in the same order as you inserted them
print(my_hash.items())  # Output: [('age', 31), ('name', 'John Doe'), ('hobbies', ['reading', 'writing', 'music'])

# Finally, you can use the hash function to calculate the hash of an object
print(hash(my_hash))  # Output: 28102212

# Hash functions are used internally by Python to determine the uniqueness of objects
print(id(my_hash))  # Output: 139888832
