from dataclasses import dataclass


@dataclass
class Product:
    """
    Product in the SauceDemo store
    """

    name: str
    description: str
    price: float
