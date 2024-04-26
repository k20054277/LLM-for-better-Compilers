
# This Python program demonstrates the use of assert and ord functions.

# Define a function to check if a character is a vowel.
def is_vowel(char):
    # Use assert to check if the character is a vowel.
    assert char.lower() in ['a', 'e', 'i', 'o', 'u']
    # Return True if the character is a vowel.
    return char.lower() in ['a', 'e', 'i', 'o', 'u']

# Iterate over a string and check if each character is a vowel.
for char in "Hello, world!":
    # Use ord to check if the character is a vowel.
    if ord(char.lower()) in range(97, 123):
        # Print the character if it is a vowel.
        print(char)
