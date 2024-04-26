
# True and bytes demonstration

# True is a boolean value that evaluates to True or False
print(True)  # Output: True

# Bytes are immutable integer values representing binary numbers
print(bytes(10))  # Output: b'10'

# You can use True and False to compare with bytes
print(True == bytes(1))  # Output: False

# You can convert True to a byte
print(int(True))  # Output: 1

# You can convert a byte to True
print(bool(10))  # Output: True

# True and False can be used in comparisons
print(True > False)  # Output: True

# Note that True and False are not interchangeable with bytes
print(True == b'10')  # Output: False
