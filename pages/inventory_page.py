from selenium.webdriver.common.by import By

from models.product import Product
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Page object representing the inventory page
    """

    INVENTORY_ITEMS = (By.CSS_SELECTOR,  "[data-test='inventory-item']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "[data-test='inventory-item-desc']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")

    def get_products(self):
        """
        Extract products information from inventory page
        """

        products = []

        items = self.find_all(self.INVENTORY_ITEMS)

        for item in items:
            name = item.find_element(*self.PRODUCT_NAME).text
            description = item.find_element(*self.PRODUCT_DESCRIPTION).text
            price = item.find_element(*self.PRODUCT_PRICE).text

            products.append(
                Product(
                    name=name,
                    description=description,
                    price=float(
                        price.replace("$", "")
                    )
                )
            )

        return products

    def get_product_by_name(self, product_name):
        """
        Find product information by product name
        """

        items = self.find_all(self.INVENTORY_ITEMS)

        for item in items:
            name = item.find_element(*self.PRODUCT_NAME).text

            if name == product_name:
                description = item.find_element(*self.PRODUCT_DESCRIPTION).text
                price = item.find_element(*self.PRODUCT_PRICE).text

                return Product(
                    name=name,
                    description=description,
                    price=float(
                        price.replace("$", "")
                    )
                )

        raise ValueError(f"Product '{product_name}' not found")

    def add_product(self, product_name):
        """
        Add product to cart
        """

        items = self.find_all(self.INVENTORY_ITEMS)

        for item in items:

            name = item.find_element(*self.PRODUCT_NAME).text

            if name == product_name:
                item.find_element(
                    *self.ADD_TO_CART_BUTTON
                ).click()

                return

        raise ValueError(f"Product '{product_name}' not found")
