import re

# Define a regular expression pattern
pattern = r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"

# Use the 'and' operator to combine the regular expression with a string
email_address = "john.doe@example.com"
if re.match(pattern, email_address):
    print("The email address is valid")
else:
    print("The email address is not valid")