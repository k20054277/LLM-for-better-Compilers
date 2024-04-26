
# Define a boolean variable 'is_even' and initialize it with False value
is_even = False

# Bitwise operation using left shift operator (<<)
number = 5
binary_representation = bin(number)[2:].zfill(32)  # Zero-padding for demonstration purposes
print("Binary representation of number 5 is:", binary_representation)

# Perform bitwise left shift operation on first bit (bit 0, index starts from 0)
is_even = is_even << 1

binary_representation = bin(int.from_bytes(bytearray([int(not not is_even)]), 'little'))[2:].zfill(32)
print("Binary representation of 'is_even' after left shift is:", binary_representation)

# The result of the left shift operation will be equivalent to setting the first bit (bit 0) to 1, which signifies even number
if int(binary_representation[0]) == 1:
    print("Number was even initially")
else:
    print("Number was odd initially")

# Set the value of 'is_even' back to False for further operations
is_even = False
