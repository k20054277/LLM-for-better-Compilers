
# Assigning None to a variable
variable = None

print("Value of variable:", variable)

# Check if a variable is equal to None
if variable is None:
    print("Variable is None")
else:
    print("Variable has a value:", variable)

# Assigning None to a dictionary key
my_dict = {"key1": "value1", "key2": "value2"}
my_dict["none_key"] = None

print("Value of 'none_key' in dictionary:", my_dict["none_key"])

# ASCII (American Standard Code for Information Interchange) is a character encoding standard. It supports 128 characters, which includes all English alphabets, digits, and various symbols.

# Displaying ASCII codes of characters
char = "A"
ascii_value = ord(char)
print("ASCII value of character '{}' is: {}".format(char, ascii_value))

# Converting ASCII code to a character
ascii_code = 65
character = chr(ascii_code)
print("Character corresponding to the ASCII code {} is: {}".format(ascii_code, character))
