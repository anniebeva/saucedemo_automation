from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    Base class for all page objects for shared functionality
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)