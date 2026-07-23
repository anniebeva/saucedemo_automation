from utils.driver import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import USERNAME, PASSWORD


def test_get_products():
    """ Test retrieving products from inventory page """

    driver = get_driver()

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(USERNAME, PASSWORD)
        inventory_page = InventoryPage(driver)

        products = inventory_page.get_products()

        assert len(products) == 6

        for product in products:
            print(product)

    finally:
        driver.quit()