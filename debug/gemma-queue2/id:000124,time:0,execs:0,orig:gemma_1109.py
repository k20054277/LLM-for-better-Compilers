
# This Python program demonstrates the use of as and bytes

# Create a string
my_string = "Hello, world!"

# Convert the string to a byte array
my_bytes = my_string.encode("utf-8")

# Print the byte array
print(my_bytes)

# Convert the byte array back to a string
my_string_from_bytes = my_bytes.decode("utf-8")

# Print the string
print(my_string_from_bytes)

# Check if the original string and the string from the bytes are equal
print(my_string == my_string_from_bytes)
