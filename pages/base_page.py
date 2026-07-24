from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions


class BasePage:
    """
    Base class for all page objects for shared functionality
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        """
        Wait for an element to be visible and return it
        """

        return self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def find_all(self, locator):
        """
        Find all matching elements
        """

        return self.driver.find_elements(*locator)

    def click(self, locator):
        """
        Click on an element
        """

        self.find(locator).click()

    def type(self, locator, text):
        """
        Type text into an input field
        """

        element = self.find(locator)
        element.clear()
        element.send_keys(text)
