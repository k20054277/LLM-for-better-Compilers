
# Demonstrating the use of and and hash in Python

# Define a dictionary
my_dict = {"apple": 10, "banana": 12, "cherry": 14}

# Check if the key "banana" is in the dictionary
if "banana" in my_dict:
    print("The key 'banana' is in the dictionary.")

# Get the value associated with the key "apple"
print("The value associated with the key 'apple' is:", my_dict["apple"])

# Hash the key "banana"
banana_hash = hash("banana")

# Print the hash value
print("The hash value of the key 'banana' is:", banana_hash)
