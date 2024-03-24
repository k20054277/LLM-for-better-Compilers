
# Define a binary number
binary_number = 0b1111_0010

# Print the original binary number
print("Original Binary Number: ", bin(binary_number)[2:])

# Use True to convert the binary number to its decimal equivalent
decimal_number = bool(binary_number) if isinstance(binary_number, int) else int(binary_number, 2)
print("Decimal Equivalent of Binary Number: ", decimal_number)

# Use bitwise NOT (represented by the tilde `~`) to invert all the bits of the binary number
inverted_number = ~binary_number

# Print the binary representation of the inverted number
print("Binary Representation of Inverted Number: ", bin(int.from_bytes(bytearray([binary_number.to_bytes(1, 'little')[0]]), 'little'))[2:])

# Use True to check if the inverted number is non-zero (i.e., if it has at least one bit set)
is_inverted_nonzero = bool(inverted_number)
print("Is Inverted Number Non-Zero? : ", is_inverted_nonzero)
