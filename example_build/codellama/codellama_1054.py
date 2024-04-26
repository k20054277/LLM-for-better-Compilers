# Using as
print(5.0 is 5) # prints True
print(5 is 5.0) # prints False

# Using bytearray
my_string = "Hello World"
byte_array = bytearray(my_string, "utf-8")
print(byte_array) # prints b'Hello World'