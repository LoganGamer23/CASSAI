from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException
import time

class infow():
    def __init__(self):
        service = Service('C:/Users/LENOVO/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        try:
            # Find the search input element
            search_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "searchInput"))
            )
            # Input the search query
            search_input.clear()
            search_input.send_keys(self.query)
            # Submit the search query
            search_input.submit()

            # Wait for the search results page to load
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "firstHeading"))
            )

            # Perform some actions, for example, print the page title
            print("Page Title:", self.driver.title)

            # Sleep indefinitely to keep the browser window open
            while True:
                time.sleep(10)  # Adjust the duration as needed
        except NoSuchWindowException:
            print("Browser window closed manually.")
        except KeyboardInterrupt:
            print("Script interrupted manually.")
        except Exception as e:
            print("Error:", e)

# Example usage:
#info = infow()
#info.get_info("iron man ")
