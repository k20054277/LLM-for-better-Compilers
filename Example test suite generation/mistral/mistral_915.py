
from selenium import webdriver

# Set up the web driver
browser = webdriver.Chrome()

# Navigate to Google
url = "https://www.google.com"
browser.get(url)

# Search for a specific term
search_term = "Python Programming"
search_box = browser.find_element_by_name("q")
search_box.send_keys(search_term)
search_button = browser.find_element_by_name("btnK")
search_button.click()

# Check if the search result title contains the expected text using 'and' logic
title = browser.title
expected_text = "Python Programming"
if "Python Programming" in title and "Google Search" in title:
    print("Search result title matches expected text.")
else:
    print("Search result title does not match expected text.")

# Close the browser window
browser.quit()
