
import BeautifulSoup

# Define the HTML content
html_content = """
<html>
  <body>
    <h1>Welcome to the world of beautiful soup!</h1>
    <p>This is a sample HTML content.</p>
  </body>
</html>
"""

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Assert the title of the page is "Welcome to the world of beautiful soup!"
assert soup.h1.text == 'Welcome to the world of beautiful soup!'

# Print the content of the paragraph
print(soup.p.text)
