from selenium import webdriver

# Initialize the web driver
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.example.com")

# Find an element on the page
element = driver.find_element_by_id("my_element")

# Use the element
print(element.text)

# Close the web driver
driver.quit()