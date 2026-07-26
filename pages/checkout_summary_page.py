from pages.base_page import BasePage

from selenium.webdriver.support.ui import WebDriverWait


class CheckoutSummaryPage(BasePage):
    """
    Checkout overview page.
    """

    PRODUCT_NAMES = ("css selector", "[data-test='inventory-item-name']")

    TOTAL_PRICE = ("css selector", "[data-test='total-label']")

    PAYMENT_INFORMATION = ("css selector", '[data-test="payment-info-value"]')

    SHIPPING_INFORMATION = ("css selector", '[data-test="shipping-info-value"]')

    TAX = ("css selector", '[data-test="tax-label"]')

    FINISH_BUTTON = ("id", "finish")

    def get_products(self):
        """
        Get products from order summary
        """

        elements = self.find_all(self.PRODUCT_NAMES)

        return [element.text for element in elements]

    def get_payment_information(self):
        """
        Get payment information
        """

        return self.find(self.PAYMENT_INFORMATION).text

    def get_shipping_information(self):
        """
        Get shipping information
        """

        return self.find(self.SHIPPING_INFORMATION).text

    def get_tax(self):
        """
        Get tax amount
        """

        return self.find(self.TAX).text

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
