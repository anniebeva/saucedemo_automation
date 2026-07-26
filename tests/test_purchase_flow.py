from pathlib import Path

from models.order import Order
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_summary_page import CheckoutSummaryPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.exports import export_order_to_xlsx, wait_pdf
from utils.product_selector import select_products

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

DOWNLOAD_FOLDER = "downloads"

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)


def test_complete_purchase(driver):
    """
    Test complete purchase flow
    """

    # 1. Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(USERNAME, PASSWORD)

    # 2-3. Add products and save information
    inventory_page = InventoryPage(driver)

    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Onesie",
    ]

    selected_products = select_products(inventory_page, products)

    # 4. Remove product from internal structure
    removed_product = selected_products[0]
    selected_products.remove(removed_product)

    # 5-6. Open cart and sync products
    cart_page = CartPage(driver)
    cart_page.open_cart()
    cart_page.remove_product(removed_product.name)

    cart_products = cart_page.get_cart_products()

    expected_names = {product.name for product in selected_products}
    actual_names = {product.name for product in cart_products}

    assert actual_names == expected_names

    # 7. Checkout
    cart_page.checkout()

    # 8. Fill checkout information
    checkout_info = CheckoutInfoPage(driver)
    checkout_info.fill_information(
        "Anna",
        "Test",
        "12345",
    )
    checkout_info.continue_checkout()

    # 9. Get order information from summary
    summary_page = CheckoutSummaryPage(driver)

    order = Order(
        products=selected_products,
        payment_information=summary_page.get_payment_information(),
        shipping_information=summary_page.get_shipping_information(),
        tax=summary_page.get_tax(),
        total=summary_page.get_total(),
    )

    summary_page.finish_order()

    # 10. Download PDF
    complete_page = CheckoutCompletePage(driver)
    complete_page.generate_pdf()

    pdf = wait_pdf(DOWNLOAD_FOLDER)

    assert pdf.endswith(".pdf")

    # 11. Export XLSX
    xlsx_file = REPORTS_DIR / "order.xlsx"

    export_order_to_xlsx(order, xlsx_file)

    assert xlsx_file.exists()
