from pages.inventory_page import InventoryPage


def test_get_products(logged_in_driver):
    """ Test retrieving products from inventory page """

    inventory_page = InventoryPage(logged_in_driver)
    products = inventory_page.get_products()

    assert len(products) == 6

    for product in products:
        print(product)
