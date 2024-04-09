
# This Python program demonstrates the use of & and bytes

# Create a byte object
my_byte = 0x1F

# Print the binary representation of the byte
print(bin(my_byte))

# Use the & operator to check if the byte is divisible by 2
if my_byte & 0x02 == 0:
    print("The byte is divisible by 2")

# Use the & operator to set the least significant bit of the byte to 0
my_byte &= 0xEF

# Print the updated binary representation of the byte
print(bin(my_byte))
