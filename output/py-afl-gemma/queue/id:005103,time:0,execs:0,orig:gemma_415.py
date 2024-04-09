
# False and Datastructure

# Define a list
my_list = [1, 2, 3, 4, 5]

# Check if the list is empty
if not my_list:
    print("The list is empty")

# Iterate over the list
for item in my_list:
    print(item)

# Check if the list contains a particular element
if 3 in my_list:
    print("The list contains the element 3")

# Create a dictionary
my_dict = {"name": "John Doe", "age": 30}

# Access the value associated with a key
print(my_dict["name"])

# Iterate over the dictionary
for key, value in my_dict.items():
    print(key + ": " + str(value))

# Check if the dictionary has a particular key
if "age" in my_dict:
    print("The dictionary has the key age")

# Output
# The list is empty
# 1
# 2
# 3
# 4
# 5
# The list contains the element 3
# name: John Doe
# age: 30
# age: 30
