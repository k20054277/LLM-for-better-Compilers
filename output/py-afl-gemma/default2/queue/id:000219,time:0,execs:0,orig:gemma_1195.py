
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.wait import WebDriverWait

# Define the desired capabilities
capabilities = webdriver.DesiredCapabilities.Chrome()

# Create a Selenium driver
driver = webdriver.Remote(capabilities=capabilities)

# Navigate to the website
driver.get("google.com")

# Wait for the page to load
WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.NAME, "lst-ib"))

# Find the search box and enter text
driver.find_element(By.NAME, "lst-ib").send_keys("Selenium")

# Click the search button
driver.find_element(By.NAME, "btnK").click()

# Print the results
for result in driver.find_elements(By.XPATH, "//div[@id='result-stats']//a"):
    print(result.text)

# Close the browser
driver.quit()
