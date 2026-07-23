from pages.inventory_page import InventoryPage
from utils.product_selector import select_products


def test_add_products_to_cart(logged_in_driver):
    """
    Test products can be added to cart
    """

    inventory_page = InventoryPage(logged_in_driver)

    product_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Onesie"
    ]

    selected_products = select_products(
        inventory_page,
        product_names
    )

    assert len(selected_products) == 3

    for product in selected_products:
        print(product)
