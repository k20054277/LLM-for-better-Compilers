
# Define a binary string
binary_string = b'1101011110110101'

# Create a bytearray from the binary string
byte_array = bytearray(binary_string)

# Manipulate the bytearray using bitwise 'and' operator with another bytearray
mask = bytearray([0x55, 0xAA])  # Define a mask for demonstration purposes
result = byte_array & mask

# Print out the original bytearray, mask and result for comparison
print("Original Bytearray : {0}".format(byte_array))
print("Mask               : {0}".format(mask))
print("Result             : {0}".format(result))
