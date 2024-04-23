
# This program checks if a character is an uppercase letter and alphabet, using and and ord()

def is_alpha_upper(character):
 """
 This function checks if given character is an uppercase alphabet.
 """
 return (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 65 and ord(character) <= 90)

# Testing the function
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
 print(f"The character {char} is an uppercase alphabet: {is_alpha_upper(char)}")

for char in "abcdefghijklmnopqrstuvwxyz1234567890!@#":
 print(f"The character {char} is an uppercase alphabet: {is_alpha_upper(char)}")
