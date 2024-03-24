
# Define two bytes variables
byte_var1 = b'Hello'  # This is a string of bytes, equivalent to byte array [72, 101, 108, 108, 111]
byte_var2 = b'World'   # This is another string of bytes, equivalent to byte array [87, 111, 114, 108, 100]

# Define a boolean variable using and operator
boolean_var = (byte_var1 == b'Hello') and (byte_var2 == b'World')

print("Byte variable 1: ", byte_var1)
print("Byte variable 2: ", byte_var2)
print("Boolean variable: ", boolean_var)

# Comparing bytes using '==' operator
if byte_var1 == byte_var2:
    print("Both variables have the same content.")
else:
    print("Variables have different content.")

# Bitwise and operation between two bytes
byte_and = byte_var1 & byte_var2
print("Bitwise AND of both bytes: ", byte_and)
