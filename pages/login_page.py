from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):
    """
    Page object representing the SauceDemo login page.
    """

    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test='login-button']")

    def open(self):
        """Open saucedemo page"""

        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """Authenticate user with provided credentials"""

        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
