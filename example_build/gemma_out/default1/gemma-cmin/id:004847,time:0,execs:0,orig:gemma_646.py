
# This Python program demonstrates the use of True and hash

# Define a boolean variable
is_active = True

# Print the value of is_active
print(is_active)

# Hash the string "abc"
hash_value = hash("abc")

# Print the hash value
print(hash_value)

# Check if two strings have the same hash value
string1 = "abc"
string2 = "abc"

if hash(string1) == hash(string2):
    print("The two strings have the same hash value")
