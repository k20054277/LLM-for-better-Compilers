
# Let's define a boolean variable 'flag' with initial value as False
flag = False

print("Boolean Value: ", flag)

# Now let's create a bytearray and initialize it with some values
my_bytearray = bytearray([1, 2, 3, 4, 5])
print("Bytearray: ", my_bytearray)

# We can change the value of a boolean variable by assigning it to True
flag = True
print("Boolean Value after assignment to True: ", flag)

# We can also change the value of a bytearray by indexing and assigning a new value
my_bytearray[0] = 10
print("Bytearray after changing first element: ", my_bytearray)

# And we can compare two boolean values or bytearrays using '=' or '==' operator
bool_value1 = True
bool_value2 = False
print("Comparison of two boolean values: ", bool_value1 == bool_value2)

bytearray1 = bytearray([1, 2, 3])
bytearray2 = bytearray([1, 2, 3])
print("Comparison of two bytearrays: ", bytearray1 == bytearray2)

# But comparing bytearrays with '=' operator checks if they are same object in memory, not their values
bytearray1_same_memory = bytearray1
print("Comparison of bytearray and itself: ", bytearray1 == bytearray1_same_memory)

# Instead use 'bytes' or '==' operator for comparing bytearrays based on their contents.
print("Comparison of bytearrays using 'bytes' or '==' operator: ", bytes(bytearray1) == bytes(bytearray2))
