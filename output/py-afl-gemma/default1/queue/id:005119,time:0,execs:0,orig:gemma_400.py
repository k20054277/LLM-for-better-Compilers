
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a Selenium session
driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

# Open a website
driver.get("google.com")

# Find the search bar and enter text
search_bar = driver.find_element(By.NAME, "q")
search_bar.clear()
search_bar.send_keys("Selenium")

# Click the search button
search_button = driver.find_element(By.NAME, "btnK")
search_button.click()

# Verify that the results page has loaded
driver.wait(2)

# Check if the results page contains the text "Selenium"
if "Selenium" in driver.page_source:
    print("The results page contains the text 'Selenium'")

# Close the browser
driver.quit()
