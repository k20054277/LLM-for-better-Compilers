
from selenium import webdriver
import time

def test_google_search():
    driver = webdriver.Firefox() # or Chrome()
    
    driver.get("https://www.google.com")
    assert "Google" in driver.title, "Google page title is not as expected."

    search_input = driver.find_element_by_name('q')
    search_input.send_keys("selenium python")
    search_input.submit()

    time.sleep(5) # Wait for the page to load completely

    assert "No results found." not in driver.page_source, "Search results are not displayed."

    first_result = driver.find_element_by_xpath("//div[@id='rso']/div[1]/div/h3/a")
    assert first_result.text != "", "First search result is empty."

    driver.quit()

if __name__ == "__main__":
    test_google_search()
