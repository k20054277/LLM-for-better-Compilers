
# Demonstrate the use of as and hash

# Define a dictionary
my_dict = {"apple": 10, "banana": 20, "cherry": 30}

# Use as to create a shorthand for the dictionary
fruits_dict = {fruit: fruit_price for fruit, fruit_price in my_dict.items()}

# Print the fruits_dict
print(fruits_dict)

# Hash the dictionary to get its hash value
hash_value = hash(fruits_dict)

# Print the hash value
print(hash_value)
