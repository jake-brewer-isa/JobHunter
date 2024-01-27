from humanLikeBrowser import HumanLikeBrowser
from .login_page import LoginPage
from .home_page import HomePage
import os

class LinkedInSite:
    def __init__(self):
        self.browser = HumanLikeBrowser()
        self.currentPage = None

    def login(self):
        username = os.environ.get("LINKEDIN_USERNAME")
        password = os.environ.get("LINKEDIN_PASSWORD")
        if not username or not password:
            raise EnvironmentError("Environment variables (LINKEDIN_USERNAME, LINKEDIN_PASSWORD) for LinkedIn credentials not set.")
        self.browser.navigate("https://www.linkedin.com/login")
        login_page = LoginPage(self.browser)
        login_page.enter_credentials(username, password)
        login_page.submit()

    def getCurrentPage(self):
        # Logic to determine the current page
        # Return an instance of the corresponding page object
        pass

    # Add more methods to interact with LinkedIn
