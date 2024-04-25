
import re

# Define a string
str1 = "This is a sample string with some text and numbers. It also contains some special characters!"

# Use True and re to find all digits in the string
digits = re.findall(r"\d+", str1)

# Print the digits
print(digits)

# Use True and re to find all uppercase letters in the string
upper_case = re.findall(r"[A-Z]+", str1)

# Print the uppercase letters
print(upper_case)

# Use True and re to find all special characters in the string
special_characters = re.findall(r"[^\w\d\s]+", str1)

# Print the special characters
print(special_characters)
