
True_bool = True
print(True_bool)  # Output: True

# Create a bytearray with the value 10
byte_arr = bytearray(10)
print(byte_arr)  # Output: b'10'

# Iterate over the elements of the bytearray
for i in range(len(byte_arr)):
    print(byte_arr[i])  # Output: 10

# Check if the bytearray is equal to True
print(byte_arr == True)  # Output: False

# Convert the bytearray to a string
print(byte_arr.decode())  # Output: 10

# Convert the bytearray to a list of integers
print(list(byte_arr))  # Output: [10]
