from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to a website
driver.get("https://www.example.com")

# Find an element on the page
element = driver.find_element_by_id("my-element")

# Check if the element is None
if element is None:
    print("Element not found")
else:
    # Do something with the element
    print(element.text)

# Close the browser
driver.quit()