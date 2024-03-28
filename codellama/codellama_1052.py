# Python program to demonstrate the use of as and ascii

# Importing the necessary modules
import string
import sys

# Taking input from the user
text = input("Enter the text: ")

# Using as() method to check if the character is a letter or not
if text.isalpha():
    print(f"The text {text} is a letter")
else:
    print(f"The text {text} is not a letter")

# Using ascii() method to convert the character to its ASCII code
print(f"ASCII code of {text}: {ord(text)}")