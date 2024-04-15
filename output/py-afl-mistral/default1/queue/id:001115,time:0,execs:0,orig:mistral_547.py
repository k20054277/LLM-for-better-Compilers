
# Define an empty dictionary
my_dict = {}

# Set some key-value pairs in the dictionary
my_dict["key1"] = "value1"
my_dict["key2"] = "value2"

# Check if the dictionary is empty
if len(my_dict) == 0:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")

# Use a key to check if it exists in the dictionary and get its value
key = "key1"
value = my_dict.get(key, True)
print(f"The value for key '{key}' is {value}.")

if key in my_dict:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")

# Modify a value in the dictionary
my_dict["key1"] = "updated_value"
print(f"The new value for key '{key}' is {my_dict['key1']}.")
