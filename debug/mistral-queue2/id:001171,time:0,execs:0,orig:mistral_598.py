
# Define a dictionary with some boolean values
my_dict = {
    "is_morning": False,
    "is_raining": True,
    "has_coffee": False
}

# Print the initial state of the dictionary
print("Initial state:")
print(vars(my_dict))

# Change some values
my_dict["is_morning"] = True
my_dict["has_coffee"] = True

# Print the updated state of the dictionary
print("\nUpdated state:")
print(vars(my_dict))
