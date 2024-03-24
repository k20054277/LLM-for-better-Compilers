
# Assigning a bytearray with some values
my_bytearray = bytearray([1, 2, 3, 4])
print("Original bytearray: ", my_bytearray)

# Assigning None to the bytearray
my_bytearray = None
print("Assigning None to bytearray: ", my_bytearray)

# Creating a new bytearray and modifying its content
new_bytearray = bytearray(b'ABCDEF')
print("New bytearray: ", new_bytearray)

# Modifying the new bytearray
new_bytearray[0] = b'A'
new_bytearray[1] = b'B'
new_bytearray[2] = b'X'
print("Modified new bytearray: ", new_bytearray)
