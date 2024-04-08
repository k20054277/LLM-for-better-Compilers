
import requests

# Define some URL to fetch
url = 'https://api.example.com/data'

# Fetch data from the URL using requests library
response = requests.get(url)

# Use response as context manager and assign its content to a variable named `content`
with response as r:
    status_code = r.status_code
    content = r.content.decode('utf-8')

# Parse the JSON content to a Python dictionary
json_data = dict(json.loads(content))

# Print some data from the JSON response
print(f'Status code: {status_code}')
print(f'Data: {json_data["key_from_json"]}')
