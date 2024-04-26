
import re

# Define a string
string = "This is a sample string with some text and numbers. It also contains a few special characters!"

# Use regular expression to find all numbers in the string
numbers = re.findall("\d+", string)

# Print the numbers
print("Numbers in the string:", numbers)

# Use regular expression to find all words in the string
words = re.findall("[a-zA-Z]+", string)

# Print the words
print("Words in the string:", words)

# Use regular expression to replace all special characters with spaces
string_without_special_characters = re.sub("[^a-zA-Z0-9\s]", " ", string)

# Print the string without special characters
print("String without special characters:", string_without_special_characters)
