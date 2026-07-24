from pages.base_page import BasePage

from selenium.webdriver.support.ui import WebDriverWait


class CheckoutSummaryPage(BasePage):
    """
    Checkout overview page.
    """

    PRODUCT_NAMES = ("css selector", "[data-test='inventory-item-name']")

    TOTAL_PRICE = ("css selector", "[data-test='total-label']")

    FINISH_BUTTON = ("id", "finish")

    def get_products(self):
        """
        Get products from order summary.
        """

        elements = self.find_all(self.PRODUCT_NAMES)

        return [element.text for element in elements]

    def get_total(self):
        """
        Get total order price
        """

        return self.find(self.TOTAL_PRICE).text

    def finish_order(self):
        """
        Complete purchase
        """

        self.click(self.FINISH_BUTTON)

        WebDriverWait(self.driver, 10).until(
            lambda driver: "checkout-complete.html" in driver.current_url
        )
