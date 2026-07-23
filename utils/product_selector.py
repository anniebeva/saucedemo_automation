from models.product import Product


def select_products(inventory_page, product_names):
    """
    Add selected products to cart and save their information
    """

    selected_products = []

    for product_name in product_names:
        product = inventory_page.get_product_by_name(product_name)

        inventory_page.add_product(product_name)

        selected_products.append(product)

    return selected_products
