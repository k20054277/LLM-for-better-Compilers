
# This program shows how to use True value and ord() function

# Using True value
is_sunny = True
print("Is it sunny outside? ", is_sunny)

# Using ord() function
character = 'A'
value = ord(character)
print(f"The ASCII value of character {character} is: {value}")

# Another example using ord() with a string
text = "Hello, World!"
for char in text:
    print(f"The ASCII value of character {char} is: {ord(char)}")
