
# Assigning False value
is_raining = False
print("Is it raining? ", is_raining)

# Printing ASCII characters
print("Printing some ASCII values:")
for i in range(123, 128): # printing special ASCII characters from 123 to 126 and 'DEL' (127)
    print(f"The ASCII value {i} represents the character: {chr(i)}")

# Comparing ASCII values using equality operator
char1 = 'A'
char2 = 'B'
print("Comparison of ASCII values:")
print(char1 == char2, "\n Char 1 is equal to char 2? ", False)
