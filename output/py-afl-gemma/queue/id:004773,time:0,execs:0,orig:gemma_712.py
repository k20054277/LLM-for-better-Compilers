
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Define the URL of the website you want to visit
url = "google.com"

# Create a Selenium driver
driver = webdriver.Chrome()

# Open the website
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)

# Find the search box and enter your query
search_box = driver.find_element(By.NAME, "q")
search_box.clear()
search_box.send_keys("Selenium")

# Click the search button
search_button = driver.find_element(By.NAME, "btnK")
search_button.click()

# Wait for the results to load
driver.implicitly_wait(10)

# Print the results
results = driver.find_elements(By.CLASS_NAME, "ZINbbc xpd O9g5cc")
for result in results:
    print(result.text)

# Close the browser
driver.quit()
