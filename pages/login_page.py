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
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
