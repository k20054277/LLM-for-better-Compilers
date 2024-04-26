
# Define a hexadecimal value for a Unicode character code
unicode_code = 0x0041

# Use chr() function to get the character from its Unicode code point
character = chr(unicode_code)
print("Character: ", character)

# Define a pair in a tuple
pair = (ord('A'), unicode_code)

# Use as keyword during unpacking the pair in a tuple
code, unicode_code_from_pair = pair

# Print both the code points for comparison
print("Unicode code from variable: ", unicode_code)
print("Unicode code from pair: ", unicode_code_from_pair)
print("Both are equal: ", (unicode_code == unicode_code_from_pair))
