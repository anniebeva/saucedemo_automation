from models.order import Order
from models.product import Product
from utils.exports import export_order_to_xlsx


def test_export_order_to_xlsx(tmp_path):
    """
    Test XLSX export
    """

    order = Order(
        products=[
            Product(
                "Backpack",
                "Description",
                "$29.99",
            )
        ],
        payment_information="SauceCard",
        shipping_information="Free Pony Express",
        tax="$2.40",
        total="$32.39",
    )

    filename = tmp_path / "order.xlsx"

    export_order_to_xlsx(order, filename)

    assert filename.exists()
