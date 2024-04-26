
# This Python program demonstrates the use of AND and hex

# Define a variable with a hexadecimal value
hex_value = 0x12

# Use the AND operator to compare the hexadecimal value with a binary value
binary_value = 0b1010

# Check if the hexadecimal value is equal to the binary value
if hex_value & binary_value == binary_value:
    print("The hexadecimal value is equal to the binary value")

# Print the hexadecimal value
print("The hexadecimal value is:", hex_value)

# Print the binary value
print("The binary value is:", binary_value)
