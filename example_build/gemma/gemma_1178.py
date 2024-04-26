
import re

# Define a string
string = "This is a string with a few words. The string has a few special characters, including $,#, and %. It also has some numbers, such as 12 and 34."

# Use as and re to find all words in the string
words = re.findall(r"\w+", string)
print(words)

# Use as and re to find all numbers in the string
numbers = re.findall(r"[0-9]+", string)
print(numbers)

# Use as and re to find all special characters in the string
special_characters = re.findall(r"[^\w\s]", string)
print(special_characters)
