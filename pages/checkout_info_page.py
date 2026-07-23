from pages.base_page import BasePage

from selenium.webdriver.support.ui import WebDriverWait


class CheckoutInfoPage(BasePage):
    """
    Checkout information page.
    """

    FIRST_NAME = ("id", "first-name")
    LAST_NAME = ("id", "last-name")
    POSTAL_CODE = ("id", "postal-code")
    CONTINUE_BUTTON = ("id", "continue")


    def fill_information(
        self,
        first_name,
        last_name,
        postal_code
    ):
        """
        Fill checkout customer information
        """

        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)

        WebDriverWait(
            self.driver,
            10
        ).until(
            lambda driver: "checkout-step-two.html" in driver.current_url
        )
