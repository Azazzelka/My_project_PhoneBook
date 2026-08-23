import pytest

from pages.home_page import HomePage
from tests_data.registration_test_data import VALID_REGISTRATION_DATA, INVALID_EMAIL_REGISTRATION_DATA, \
    INVALID_PASSWORD_REGISTRATION_DATA


@pytest.mark.parametrize("data", VALID_REGISTRATION_DATA)
def test_registration_valid_data(driver,data):
    login_page = HomePage(driver).open().open_login_page()

    login_page.fill_registration_form(data)
    assert login_page.is_logged()

@pytest.mark.parametrize("data", INVALID_EMAIL_REGISTRATION_DATA)
def test_registration_invalid_email(driver,data):
    login_page = HomePage(driver).open().open_login_page()

    login_page.fill_registration_form(data)
    assert "Email must contains one" in login_page.get_alert_text()
    login_page.alert_accept()
    assert not login_page.is_logged()

@pytest.mark.parametrize("data", INVALID_PASSWORD_REGISTRATION_DATA)
def test_registration_invalid_password(driver,data):
    login_page = HomePage(driver).open().open_login_page()

    login_page.fill_registration_form(data)
    assert "Email must contains one" in login_page.get_alert_text()
    login_page.alert_accept()
    assert not login_page.is_logged()