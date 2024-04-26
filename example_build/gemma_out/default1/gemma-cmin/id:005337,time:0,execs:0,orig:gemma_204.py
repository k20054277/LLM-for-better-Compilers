
hex_value = 0x12

# Print the hexadecimal value
print("Hex value:", hex_value)

# Convert the hexadecimal value to a binary value
binary_value = int(hex_value, 16)

# Print the binary value
print("Binary value:", binary_value)

# Use the and operator to compare the binary values
if binary_value & 0x08 == 0x08:
    print("The binary value has a set bit at the second position")

# Output:
# Hex value: 18
# Binary value: 24
# The binary value has a set bit at the second position
