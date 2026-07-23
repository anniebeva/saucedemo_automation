from dataclasses import dataclass


@dataclass
class Product:
    """
    class a product in the SauceDemo store
    """

    name: str
    description: str
    price: float
