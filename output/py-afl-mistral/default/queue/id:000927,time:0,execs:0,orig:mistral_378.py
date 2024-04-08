
from selenium import webdriver

def find_element_by_css(driver, css_selector):
    try:
        return driver.find_element_by_css_name(css_selector)
    except Exception as e:
        print(f"No element found with CSS selector: {css_selector}. Error: {e}")
        return None

def main():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    
    # Navigate to a webpage
    driver.get("https://www.google.com")

    # Find the search box element and enter a search query
    search_box = find_element_by_css(driver, "name='q'")
    if search_box is not None:
        search_box.send_keys("Selenium Python")
        search_button = find_element_by_css(driver, "name='btnK'")
        if search_button is not None:
            search_button.click()
        else:
            print("Search button not found!")
    else:
        print("Search box not found!")
    
    # Quit the Chrome driver
    driver.quit()

if __name__ == "__main__":
    main()
