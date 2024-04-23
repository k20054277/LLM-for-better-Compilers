# Demonstrate the use of as and bytes in Python

# Import the necessary modules
import struct

# Create a sample byte string
sample_byte_string = b'Hello World!'

# Use the as method to convert the byte string to an integer
integer_value = sample_byte_string.as(struct.Int32)
print("Integer value:", integer_value)

# Use the bytes method to convert the integer back to a byte string
byte_string_value = struct.pack('i', integer_value)
print("Byte string value:", byte_string_value)