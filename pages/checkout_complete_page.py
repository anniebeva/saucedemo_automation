from pages.base_page import BasePage

from selenium.webdriver.support.ui import WebDriverWait


class CheckoutCompletePage(BasePage):
    """
    Order completion page
    """

    COMPLETE_MESSAGE = ("css selector", "[data-test='complete-header']")

    BACK_HOME_BUTTON = ("id", "back-to-products")

    GENERATE_PDF_BUTTON = ("id", "generate-pdf-order")

    def get_success_message(self):
        """
        Get order confirmation message
        """

        return self.find(self.COMPLETE_MESSAGE).text

    def generate_pdf(self):
        """
        Download order PDF.
        """

        self.click(self.GENERATE_PDF_BUTTON)

    def back_home(self):
        """
        Return to products page
        """

        self.click(self.BACK_HOME_BUTTON)

        WebDriverWait(self.driver, 10).until(
            lambda driver: "inventory.html" in driver.current_url
        )
