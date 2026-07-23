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
