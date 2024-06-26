
import re

def extract_email(text):
    # Define the regular expression pattern for email addresses
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    
    # Search for matches in the text using re.search()
    match = re.search(pattern, text)
    
    # Check if a match was found
    if match:
        # Use as keyword to assign captured groups to variables
        email = match.group(0)
        user, domain = match.groups(2, 3)
        
        print("Email address extracted: {}".format(email))
        print("User: {}, Domain: {}".format(user, domain))
    else:
        print("No email address found in the text.")

# Test the extract_email() function with some sample strings
text1 = "Please send your feedback to john.doe@example.com"
extract_email(text1)

text2 = "My email is jane_doe@acme.co.uk and I'll be there tomorrow."
extract_email(text2)
