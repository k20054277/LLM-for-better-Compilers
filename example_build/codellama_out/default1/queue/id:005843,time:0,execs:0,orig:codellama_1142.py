from selenium import webdriver

# Set up Selenium WebDriver
driver = webdriver.Firefox()

# Navigate to the website you want to scrape
driver.get("https://www.example.com")

# Find the element you want to scrape using CSS selector
element = driver.find_element_by_css_selector("#some-id")

# Use as() method to convert the element to a string
string = element.as(str)

# Print the scraped data
print(string)

# Close the WebDriver
driver.quit()