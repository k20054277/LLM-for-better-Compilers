
# Assigning an alias using as
import urllib.request as url

url = 'https://example.com'
response = url.urlopen(url)
data = response.read()
content = data.decode('utf-8') as str
print(content)
