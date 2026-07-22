from utils.driver import get_driver


def test_open_saucedemo():
    """Test browser access"""

    driver = get_driver()
    driver.get("https://www.saucedemo.com/")

    assert "Swag Labs" in driver.title

    driver.quit()