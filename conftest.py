import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.home_page import HomePage
from tests_data.login_test_data import VALID_LOGIN_DATA_1


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

@pytest.fixture
def user():
    return VALID_LOGIN_DATA_1

@pytest.fixture
def authenticated_driver(driver, user):
    login_page = HomePage(driver).open().open_login_page()
    login_page.fill_login_form(user)

    return driver

