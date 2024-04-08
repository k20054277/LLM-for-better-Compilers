my_dict = {}

# Adding a new key-value pair to the dictionary
my_dict["name"] = "Alice"

# Accessing a value in the dictionary using the dot notation
print(my_dict.name)  # Output: Alice

# Using **= to update a value in the dictionary
my_dict["age"] = 25

# Accessing a value in the dictionary using the bracket notation
print(my_dict["age"])  # Output: 25

# Using as to convert an object to a dictionary
x = {"name": "Bob", "age": 30}
y = x.asDict()

# Printing the contents of the converted dictionary
print(y)  # Output: {'name': 'Bob', 'age': 30}