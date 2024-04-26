
from bs4 import BeautifulSoup

# HTML content
html_content = """
<div id="container">
    <h1>Welcome to the world of BeautifulSoup!</h1>
    <p>This is a sample HTML document.</p>
    <a href="example.com">Click here to visit example.com</a>
</div>
"""

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find the heading element
heading = soup.find("h1")

# Print the heading element's text
print(heading.text)

# Find the paragraph element
paragraph = soup.find("p")

# Print the paragraph element's text
print(paragraph.text)

# Find the anchor element
anchor = soup.find("a")

# Print the anchor element's text and href
print("Text:", anchor.text)
print("Href:", anchor["href"])
