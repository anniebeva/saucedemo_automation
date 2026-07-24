import os
import time

from openpyxl import Workbook

from models.order import Order


def export_order_to_xlsx(order: Order, filename: str):
    """
    Export order information to XLSX
    """

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Order"

    sheet.append(
        [
            "Product",
            "Description",
            "Price",
        ]
    )

    for product in order.products:
        sheet.append(
            [
                product.name,
                product.description,
                product.price,
            ]
        )

    sheet.append([])
    sheet.append(
        [
            "Payment Information",
            order.payment_information,
        ]
    )

    sheet.append(
        [
            "Shipping Information",
            order.shipping_information,
        ]
    )

    sheet.append(
        [
            "Tax",
            order.tax,
        ]
    )

    sheet.append(
        [
            "Total",
            order.total,
        ]
    )

    workbook.save(filename)


def wait_pdf(folder, timeout=10):
    """
    Wait until PDF is downloaded
    """

    end = time.time() + timeout

    while time.time() < end:

        for file in os.listdir(folder):
            if file.endswith(".pdf"):
                return file

        time.sleep(0.5)

    raise TimeoutError("PDF was not downloaded.")

