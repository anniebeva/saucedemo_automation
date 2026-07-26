# SauceDemo Automation

Automation project for testing the checkout flow on [SauceDemo](https://www.saucedemo.com/)

The project implements an end-to-end purchase scenario:
- User authentication
- Product selection
- Cart validation and synchronization
- Checkout process
- Order confirmation
- PDF order generation
- XLSX report export

## Stack

- Python 3.13
- Selenium WebDriver
- Pytest
- webdriver-manager
- openpyxl

## Project structure

```
saucedemo_automation/
│
├── pages/                         
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_info_page.py
│   ├── checkout_summary_page.py
│   └── checkout_complete_page.py
│
├── models/                      
│   ├── product.py
│   └── order.py
│
├── utils/                        
│   ├── exports.py
│   ├── driver.py
│   └── product_selector.py
│
├── tests/                       
│   ├── test_checkout.py
│   └── test_purchase_flow.py
│
├── downloads/                    
│
├── reports/                   
│
├── conftest.py                    
├── requirements.txt          
└── README.md
```


## Installation

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Create and activate virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running tests

Run all tests:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_purchase_flow.py -v
```

## Test scenario

The main end-to-end scenario covers the complete purchase flow.

The implementation can be found in `tests/test_purchase_flow.py`

1. User authentication
2. Adding multiple products to the cart
3. Saving product information internally:
   - name
   - description
   - price
4. Removing a product from the internal data structure
5. Opening the cart
6. Synchronizing cart contents with expected data
7. Proceeding to checkout
8. Filling customer information
9. Collecting order summary data:
   - Payment Information
   - Shipping Information
   - Tax
   - Total
10. Completing the purchase
11. Generating PDF order confirmation
12. Exporting order data to XLSX