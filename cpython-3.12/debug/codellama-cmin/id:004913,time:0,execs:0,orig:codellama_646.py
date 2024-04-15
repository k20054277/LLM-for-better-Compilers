# This program demonstrates the use of True and bytes in Python

# True represents the logical value "True" or "False"
print(True)       # Output: True
print(not True)   # Output: False

# Bytes are sequences of 8-bit unsigned integers
bytes_object = b'hello world'
print(bytes_object)    # Output: b'hello world'

# You can use the bytes() function to create a byte sequence from a string
string_object = 'hello world'
byte_sequence = bytes(string_object, 'utf-8')
print(byte_sequence)   # Output: b'hello world'

# You can also use the bytes literal notation (prefixed with "b") to create a byte sequence from a string
byte_sequence2 = b'hello world'
print(byte_sequence2)  # Output: b'hello world'