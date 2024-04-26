
import requests

# Make an HTTP request to Google search
response = requests.get("https://www.google.com/search?q=requests+library")

# Response contains several useful attributes, we use the 'content' attribute to get the HTML content
html_content = response.content

# Assign aliases for easier handling and readability
status_code = response.status_code
headers = response.headers

print("Status code: ", status_code)
print("Headers:\n", headers)
print("\nHTML content (first 100 characters):\n")
print(html_content[0:100])
