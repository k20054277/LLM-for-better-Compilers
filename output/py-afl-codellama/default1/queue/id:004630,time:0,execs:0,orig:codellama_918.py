from selenium import webdriver
import time

# Set up the Chrome driver
driver = webdriver.Chrome()

# Go to the website
driver.get("https://www.example.com")

# Wait for the page to load
time.sleep(5)

# Find the elements that contain the data we want to scrape
elements = driver.find_elements_by_css_selector(".data-element")

# Loop through each element and extract the text
for element in elements:
    # Use 'and' to combine multiple conditions
    if "Condition 1" in element.text and "Condition 2" in element.text:
        print(element.text)

# Quit the driver
driver.quit()