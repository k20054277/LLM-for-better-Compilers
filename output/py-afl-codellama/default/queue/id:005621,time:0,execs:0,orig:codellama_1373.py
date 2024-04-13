from selenium import webdriver

# Initialize the web driver
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("http://www.example.com")

# Use assert to check if an element is present on the page
assert driver.find_element_by_xpath("//h1").is_displayed()

# Use assert to check if an element has a specific text
assert driver.find_element_by_xpath("//h1").text == "Example"

# Close the web driver
driver.quit()