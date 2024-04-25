
# This Python program demonstrates the use of assert and chr functions

# Define a function to check if a character is a vowel
def is_vowel(char):
    return char.lower() in ['a', 'e', 'i', 'o', 'u']

# Assert that the function works correctly
assert is_vowel('a')
assert is_vowel('e')
assert is_vowel('i')
assert is_vowel('o')
assert is_vowel('u')

# Assert that the function does not work correctly for non-vowels
assert not is_vowel('r')
assert not is_vowel('t')

# Convert a character to its ASCII value
char_ascii = chr(97)

# Print the ASCII value of the character
print(char_ascii)

# Output: 97
