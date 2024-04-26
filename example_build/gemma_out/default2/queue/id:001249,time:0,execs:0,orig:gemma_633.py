
# True and dict

# Create a dictionary
my_dict = {"key1": True, "key2": False, "key3": 10}

# Print the values of the dictionary
print(my_dict)

# Check if the value associated with key1 is True
print(my_dict["key1"] is True)

# Iterate over the dictionary
for key, value in my_dict.items():
    print(key + ": " + str(value))
