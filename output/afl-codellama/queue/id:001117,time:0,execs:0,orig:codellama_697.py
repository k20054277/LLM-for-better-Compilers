import re

# Use True to create a boolean variable
is_true = True

# Use re to search for a pattern in a string
pattern = r'^Hello$'
text = 'Hello World!'
if re.search(pattern, text):
    print("Match found!")
else:
    print("No match found.")