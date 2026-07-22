from utils.driver import get_driver
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


def test_successful_login():
    """Test login with valid credentials"""

    driver = get_driver()

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(USERNAME, PASSWORD)

        assert "inventory" in driver.current_url

    finally:
        driver.quit()