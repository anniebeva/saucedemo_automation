import pytest

from utils.driver import get_driver
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


@pytest.fixture
def driver():
    """Create browser instance"""

    driver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    """
    Open application with authenticated user.
    """

    driver.get("https://www.saucedemo.com/")

    # Clear application state
    driver.execute_script(
        "window.localStorage.clear();"
    )

    login_page = LoginPage(driver)

    login_page.login(
        USERNAME,
        PASSWORD
    )

    return driver