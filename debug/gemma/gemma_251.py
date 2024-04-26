
import re

# Define a string
string = "This is a string with a few words and numbers. It also has some special characters!"

# Use AND to match words and numbers
pattern = r"\w+|\d+"

# Search for the pattern in the string
matches = re.findall(pattern, string)

# Print the matches
print(matches)

# Use AND to match words and numbers, but exclude special characters
pattern = r"\w+|\d+|[^\w\d]"

# Search for the pattern in the string
matches = re.findall(pattern, string)

# Print the matches
print(matches)
