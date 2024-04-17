
import urllib.request
import re

def get_numbers_from_url(url):
    """
    Fetches the HTML content from given URL and extracts numbers using regex.
    :param url: str, URL to fetch the HTML content from
    :return: list, list of numbers present in the HTML content
    """

    try:
        html = urllib.request.urlopen(url).read().decode()
    except Exception as e:
        print(f"Error while fetching URL: {e}")
        return []

    pattern = re.compile(r'\d+')
    numbers = pattern.findall(html)

    assert len(numbers) > 0, "No numbers found in the HTML content"

    return numbers

if __name__ == "__main__":
    url = "https://example.com/numbers_page"
    numbers = get_numbers_from_url(url)
    print("Numbers from URL:", numbers)
