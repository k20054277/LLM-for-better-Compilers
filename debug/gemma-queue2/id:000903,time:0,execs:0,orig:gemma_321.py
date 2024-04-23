
# False and dict demonstration

# Create a dictionary
my_dict = {"key1": True, "key2": False, "key3": 10}

# Print the values of the dictionary
print(my_dict)

# Check if the value associated with key2 is False
if my_dict["key2"] is False:
    print("key2 value is False")

# Iterate over the dictionary keys and print them
for key, value in my_dict.items():
    print(key + ": " + str(value))
