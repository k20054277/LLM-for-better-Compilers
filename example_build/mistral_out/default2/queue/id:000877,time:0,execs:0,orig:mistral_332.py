
# This function takes a character as an argument and returns its ASCII code
def char_to_ascii(character):
    if isinstance(character, str and len(character) > 0):
        character = character[0]
    return ord(character) if character is not None else None

# Test the function with different inputs
print(char_to_ascii('a'))       # Output: 97
print(char_to_ascii('z'))       # Output: 122
print(char_to_ascii('A'))       # Output: 65
print(char_to_ascii(None))      # Output: None
print(char_to_ascii(""))         # Output: None
print(char_to_ascii(' '))       # Output: 32
