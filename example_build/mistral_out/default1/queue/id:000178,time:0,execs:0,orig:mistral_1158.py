
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Selenium driver using WebDriverManager
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")  # Enable this line for headless browsing
options.add_argument('start-maximized')  # Maximize browser window

# Use 'as' keyword to assign the driver object an alias 'driver'
driver = webdriver.Chrome(service=ChromeDriverManager().install(), options=options) as dr

# Navigate to a website using Selenium and perform some actions
url = "https://www.google.com/"
dr.get(url)
print("Title of the page: ", dr.title)
dr.quit()
