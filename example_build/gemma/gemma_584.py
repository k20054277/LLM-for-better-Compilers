
# None and {} demonstration

# None

none_value = None

print(none_value is None)  # Output: True

# Empty Dictionary

empty_dict = {}

print(empty_dict == {})  # Output: True

# Adding key-value pair to an empty dictionary

empty_dict["key"] = "value"

print(empty_dict)  # Output: {'key': 'value'}

# Checking if a key is in a dictionary

print("key" in empty_dict)  # Output: True

# Iterating over a dictionary

for key, value in empty_dict.items():
    print(key, ": ", value)  # Output: key: value

# Removing key-value pair from a dictionary

empty_dict.pop("key")

print(empty_dict)  # Output: {}