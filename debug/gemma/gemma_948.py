
import bs4

# Define the HTML content
html_content = """
<html>
  <body>
    <h1>Welcome to the world of beautifulsoup!</h1>
    <p>This is a sample HTML document.</p>
  </body>
</html>
"""

# Create a BeautifulSoup object from the HTML content
soup = bs4. BeautifulSoup(html_content, 'html.parser')

# Find the heading element and print its text
print(soup.h1.text)

# Find all paragraph elements and print their text
for p in soup.find_all('p'):
    print(p.text)
