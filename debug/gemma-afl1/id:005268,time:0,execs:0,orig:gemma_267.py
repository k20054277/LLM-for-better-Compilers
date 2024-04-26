
import BeautifulSoup

# HTML content
html_content = """
<html>
    <body>
        <h1>Hello, world!</h1>
        <p>This is a paragraph of text.</p>
    </body>
</html>
"""

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the heading tag and print its text
print(soup.h1.text)

# Find the paragraph tag and print its text
print(soup.p.text)
