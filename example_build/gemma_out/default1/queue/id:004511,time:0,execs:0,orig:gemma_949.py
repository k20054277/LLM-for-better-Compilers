
import selenium
from selenium import webdriver

# Create a Chrome session
driver = webdriver.Chrome()

# Open Google search page
driver.get("google.com")

# Enter search query and submit
driver.find_element_by_name("q").send_keys("Selenium")
driver.find_element_by_name("q").submit()

# Print results
print(driver.page_source)

# Close the browser
driver.quit()
