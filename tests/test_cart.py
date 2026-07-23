from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

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


def test_remove_product_from_cart(logged_in_driver):
    """Test product removal from cart"""

    inventory_page = InventoryPage(logged_in_driver)

    product_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Onesie",
    ]

    select_products(inventory_page, product_names)

    cart_page = CartPage(logged_in_driver)
    cart_page.open_cart()

    cart_page.remove_product(
        "Sauce Labs Backpack"
    )

    products = cart_page.get_cart_products()

    names = {
        product.name
        for product in products
    }

    assert "Sauce Labs Backpack" not in names
