
# Create a dictionary
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# Set the value of a key to False
my_dict["key1"] = False

print("Dictionary before deleting 'key1':")
print(my_dict)

# Use del to delete 'key1'
del my_dict["key1"]

print("\nDictionary after deleting 'key1':")
print(my_dict)
