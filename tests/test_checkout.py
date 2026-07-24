from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_summary_page import CheckoutSummaryPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_checkout_information_form(logged_in_driver):
    """
    Test filling checkout information form
    """

    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_product("Sauce Labs Backpack")

    cart_page = CartPage(logged_in_driver)

    cart_page.open_cart()
    cart_page.checkout()

    checkout_info = CheckoutInfoPage(logged_in_driver)

    checkout_info.fill_information("Anna", "Test", "12345")

    checkout_info.continue_checkout()
    assert "checkout-step-two" in logged_in_driver.current_url


def test_checkout_summary(logged_in_driver):
    """
    Test order summary page
    """

    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_product("Sauce Labs Backpack")

    cart_page = CartPage(logged_in_driver)

    cart_page.open_cart()
    cart_page.checkout()

    checkout_info = CheckoutInfoPage(logged_in_driver)

    checkout_info.fill_information("Anna", "Test", "12345")

    checkout_info.continue_checkout()
    summary_page = CheckoutSummaryPage(logged_in_driver)

    products = summary_page.get_products()
    assert "Sauce Labs Backpack" in products

    summary_page.finish_order()
    assert "checkout-complete" in logged_in_driver.current_url


def test_checkout_complete(logged_in_driver):
    """
    Test order completed page
    """

    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_product("Sauce Labs Backpack")

    cart_page = CartPage(logged_in_driver)
    cart_page.open_cart()
    cart_page.checkout()

    checkout_info = CheckoutInfoPage(logged_in_driver)
    checkout_info.fill_information("Anna", "Test", "12345")
    checkout_info.continue_checkout()

    summary_page = CheckoutSummaryPage(logged_in_driver)
    summary_page.finish_order()

    complete_page = CheckoutCompletePage(logged_in_driver)
    assert complete_page.get_success_message() == ("Thank you for your order!")

    complete_page.back_home()
    assert "inventory.html" in logged_in_driver.current_url
