
import requests
from bs4 import BeautifulSoup

# Fetch the HTML content from a given URL
def get_html(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError("Failed : " + url)
    return response.text

# Parse the HTML content using BeautifulSoup
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Assertion function to check if a specific tag exists in the parsed HTML
def assert_tag_exists(soup, tag_name):
    tags = soup.find_all(True, tag=tag_name)
    assert len(tags) > 0, f"Tag '{tag_name}' not found in the HTML!"

# Main function to test our functions
def main():
    url = "https://example.com"
    html = get_html(url)
    soup = parse_html(html)

    assert_tag_exists(soup, 'html')
    assert_tag_exists(soup, 'head')
    assert_tag_exists(soup, 'title')
    assert_tag_exists(soup, 'body')

if __name__ == "__main__":
    main()
