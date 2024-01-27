import os
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller

logger = logging.getLogger(__name__)

class HumanLikeBrowser:
    def __init__(self):
        # Automatically install or update ChromeDriver
        chromedriver_autoinstaller.install()
        self.driver = self.initialize_driver()

    def initialize_driver(self):
        try:
            logger.debug("Initializing ChromeDriver")
            driver = webdriver.Chrome()
            return driver
        except Exception as e:
            logger.error(f"Error initializing ChromeDriver: {e}")
            raise
            
    def open_website(self, url):
        if self.driver:
            self.driver.get(url)
            logger.info(f"Opened website: {url}")

    def wait_for_element(self, by, value, timeout=10):
        if self.driver:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located((by, value)))
            return element

    def close(self):
        if self.driver:
            self.driver.quit()

# Example usage
if __name__ == "__main__":
    try:
        browser = HumanLikeBrowser()
        browser.open_website("https://www.example.com")
        # Add more actions here
        browser.close()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
