
# This Python program demonstrates the use of and and bytes

# Define a byte variable
my_byte = 0b1010

# Check if the byte is even using and
if my_byte & 0b1000 == 0b1000:
  print("The byte is even")

# Convert the byte to a string
my_byte_str = bin(my_byte).replace("0b", "")

# Print the binary representation of the byte
print("The binary representation of the byte is:", my_byte_str)
