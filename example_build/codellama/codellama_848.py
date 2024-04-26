# Demonstrating the use of 'and' with bytearray

# Creating two bytearrays
a = bytearray(b"abcd")
b = bytearray(b"cdefg")

# Using 'and' to find common characters between the two arrays
print("Common characters:", a & b)