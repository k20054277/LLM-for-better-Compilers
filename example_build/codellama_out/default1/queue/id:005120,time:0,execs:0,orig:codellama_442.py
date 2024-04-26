# Demonstration of using None and bytes in Python

# Using None
print(None)  # Output: None

# Using bytes
my_bytes = b'hello world'
print(type(my_bytes))  # Output: <class 'bytes'>
print(len(my_bytes))   # Output: 11
print(my_bytes.decode('utf-8'))  # Output: 'hello world'