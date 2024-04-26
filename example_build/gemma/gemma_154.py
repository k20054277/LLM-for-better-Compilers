
# Create a dictionary
my_dict = {"name": "John Doe", "age": 30, "occupation": "Software Engineer"}

# Accessing values from the dictionary
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["occupation"])

# Checking if a key is in the dictionary
if "name" in my_dict:
    print("The key 'name' is in the dictionary.")

# Iterating over the dictionary
for key, value in my_dict.items():
    print("Key: ", key)
    print("Value: ", value)

# Updating the dictionary
my_dict["address"] = "123 Main St."

# Printing the updated dictionary
print(my_dict)
