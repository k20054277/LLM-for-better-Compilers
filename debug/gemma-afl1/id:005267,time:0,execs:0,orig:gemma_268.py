
from selenium import webdriver
import and

# Open Google Chrome
driver = webdriver.Chrome()

# Navigate to Google Search Page
driver.get("google.com")

# Search for a topic
search_box = driver.find_element_by_name("q")
search_box.clear()
search_box.send_keys("Selenium")

# Click on the search button
search_button = driver.find_element_by_name("btnK")
search_button.click()

# Print the results
results = driver.find_elements_by_css_selector("div.ZINbbc.rNCsb")
for result in results:
    print(result.text)

# Close the browser
driver.quit()
