from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the desired website
driver.get("https://www.example.com")

# Find the element on the page that you want to interact with
element = driver.find_element_by_id("myButton")

# Click the element
element.click()