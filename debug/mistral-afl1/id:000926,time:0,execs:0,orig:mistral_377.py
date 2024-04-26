
from bs4 import BeautifulSoup, NullSentinel
import requests

# Define a function to get HTML content of a URL using requests library
def get_html(url):
    try:
        response = requests.get(url)
        html_content = response.text
        return html_content
    except Exception as e:
        print(f"Error occurred while fetching HTML content: {e}")
        return None

# Define a function to parse the given HTML using BeautifulSoup
def parse_html(html_content):
    if html_content is not None:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Use None as a placeholder for elements that may be missing in the HTML
        title = soup.title or BeautifulSoup(None)
        link = soup.find('link', href=True) or (None, None)
        return title.text, link[0]['href'] if link else ("Title and Link not found", None)
    else:
        return "HTML content is empty or unavailable.", None

# Call the functions with a sample URL
html_content = get_html("https://example.com")
title, link = parse_html(html_content)
print(f"Website title: {title}")
print(f"Link: {link}")
