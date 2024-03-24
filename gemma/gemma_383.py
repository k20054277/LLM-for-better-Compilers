
import re

# Define a string
string = "This is a string with false information and some regex patterns."

# Use False to check if the string contains the word "false"
if False:
    print("The string contains the word 'false'.")

# Use re.search to find the regex pattern "false" in the string
if re.search("false", string):
    print("The string contains the word 'false'.")

# Output
# The string does not contain the word 'false'.
