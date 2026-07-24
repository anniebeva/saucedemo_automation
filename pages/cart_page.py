from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from models.product import Product

from selenium.webdriver.support.ui import WebDriverWait


class CartPage(BasePage):
    """
    Page Object for shopping cart page
    """

    CART_BUTTON = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    CART_ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "[data-test='inventory-item-desc']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[data-test^='remove']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")

    def open_cart(self):
        """
        Open shopping cart
        """

        self.click(self.CART_BUTTON)

        WebDriverWait(self.driver, 10).until(
            lambda driver: "cart.html" in driver.current_url
        )

    def get_cart_products(self):
        """
        Get products currently in cart
        """

        products = []

        items = self.find_all(self.CART_ITEMS)

        for item in items:
            name = item.find_element(*self.PRODUCT_NAME).text
            description = item.find_element(*self.PRODUCT_DESCRIPTION).text
            price = item.find_element(*self.PRODUCT_PRICE).text

            products.append(
                Product(
                    name=name,
                    description=description,
                    price=float(price.replace("$", "")),
                )
            )

        return products

    def remove_product(self, product_name):
        """
        Remove product from cart by name
        """

        items = self.find_all(self.CART_ITEMS)

        for item in items:
            name = item.find_element(*self.PRODUCT_NAME).text

            if name == product_name:
                remove_button = item.find_element(By.CSS_SELECTOR, "button")

                remove_button.click()
                return

        raise ValueError(f"Product '{product_name}' not found")

    def checkout(self):
        """
        Proceed to checkout
        """

        self.click(self.CHECKOUT_BUTTON)
