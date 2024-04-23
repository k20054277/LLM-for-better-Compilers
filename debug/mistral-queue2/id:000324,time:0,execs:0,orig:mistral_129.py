
from selenium import webdriver

# Create a new Chrome browser instance
browser = webdriver.Chrome()

# Navigate to a page that does not exist
try:
    browser.get("http://invalid-url.com")
    title = browser.title
except Exception as e:
    print(f"An error occurred while loading the page: {e}")
    title = "Error Page"  # Set title to an error message for demonstration purposes

# Check if title is equal to "404 Error", and if not, print an error message
if title != "404 Error":
    print("The title of the loaded page does not match the expected value.")

browser.quit()  # Close the browser window after the script runs
