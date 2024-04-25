# Demonstrate the use of "and" operator with bytearray

byte_string = b'10101010'
byte_array = bytearray(byte_string)

print("Original byte string:", byte_string)
print("Byte array:", byte_array)

# Use "and" operator to perform bitwise AND operation on the elements of the byte array
result = byte_array & 0xF0

print("Result of bitwise AND operation:", result)