from dataclasses import dataclass

from models.product import Product


@dataclass
class Order:
    """
    Store order information after checkout
    """

    products: list[Product]
    payment_information: str
    shipping_information: str
    tax: str
    total: str
