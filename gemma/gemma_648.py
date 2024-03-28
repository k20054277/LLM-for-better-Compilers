
True_hex = True

# Convert True to hex
print(True_hex.hex())

# Output: True
# Output: 1

# Convert a hex number to True
print(True_hex.is_hex("0x1"))

# Output: True

# Convert a non-hex number to False
print(True_hex.is_hex("1"))

# Output: False
