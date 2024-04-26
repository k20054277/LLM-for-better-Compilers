
from selenium import webdriver

# Set up the webdriver
browser = webdriver.Chrome()

# Close the browser if it's already open (Boolean check)
if not browser.is_displayed():
    print("Browser is already open.")
else:
    print("Starting new browser instance...")

# Navigate to a website
url = "https://www.google.com"
browser.get(url)

# Perform some actions (Boolean checks and Selenium usage)
search_box = browser.find_element_by_name("q")
search_box.send_keys("Selenium Python", keys.SPACE)
search_button = browser.find_element_by_name("btnK")
search_button.click()

# Check if the search results are displayed (Boolean check)
if not browser.find_elements_by_xpath("//h3[@class='LC20lb']"):
    print("Search results not found.")
else:
    first_result = browser.find_element_by_xpath("//h3[@class='LC20lb']")
    print(f"First search result: {first_result.text}")

# Quit the browser instance
browser.quit()
