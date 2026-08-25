import pytest

from pages.home_page import HomePage
from tests_data.login_test_data import VALID_LOGIN_DATA, INVALID_EMAIL_DATA, INVALID_PASSWORD_DATA, \
    UNREGISTERED_VALID_LOGIN_DATA


@pytest.mark.parametrize("data", VALID_LOGIN_DATA)
def test_login_positive(driver, data):
    login_page = HomePage(driver).open().open_login_page()

    login_page.fill_email(data.email)
    login_page.fill_password(data.password)
    login_page.submit_login()

    assert login_page.is_logged()
@pytest.mark.parametrize("data", INVALID_EMAIL_DATA)
def test_login_wrong_email(driver, data):
    login_page = HomePage(driver).open().open_login_page()

    login_page.fill_login_form(data)

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.alert_accept()
    assert not login_page.is_logged()

@pytest.mark.parametrize("data", INVALID_PASSWORD_DATA)
def test_login_wrong_password(driver,data):
    login_page = HomePage(driver).open().open_login_page()

    login_page.fill_login_form(data)

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.alert_accept()
    assert not login_page.is_logged()

@pytest.mark.parametrize("data", UNREGISTERED_VALID_LOGIN_DATA)
def test_login_valid_not_registered_data(driver,data):
    login_page = HomePage(driver).open().open_login_page()

    login_page.fill_login_form(data)

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.alert_accept()
    assert not login_page.is_logged(1)