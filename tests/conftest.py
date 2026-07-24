import pytest

from utils.driver import get_driver
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

from selenium import webdriver


@pytest.fixture
def driver():
    """
    Create and configure Chrome WebDriver
    """

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=PasswordLeakDetection")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    """
    Open application with authenticated user
    """

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(USERNAME, PASSWORD)

    return driver
