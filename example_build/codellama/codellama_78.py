# This program demonstrates the use of 'and' and 'ascii'

# Importing the necessary modules
import ascii

# Printing the ASCII value of the character 'a'
print(ord('a')) # Output: 97

# Printing the ASCII value of the character 'A'
print(ord('A')) # Output: 65

# Using 'and' to check if a number is even and less than 10
num = 8
if num % 2 == 0 and num < 10:
    print("The number is even and less than 10")
else:
    print("The number is not even or greater than 10")