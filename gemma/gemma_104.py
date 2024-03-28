
# This Python program demonstrates the use of the and operator and the chr function.

# Define a character.
character = chr(97)

# Print the character.
print(character)

# Check if the character is lowercase.
if character.islower():
  print("The character is lowercase.")

# Convert the character to uppercase.
character_upper = character.upper()

# Print the uppercase character.
print(character_upper)

# Print the ASCII value of the character.
print("The ASCII value of the character is:", ord(character))
