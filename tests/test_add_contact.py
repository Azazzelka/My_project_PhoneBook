from time import sleep

import pytest
from selenium.common import TimeoutException

from pages.home_page import HomePage
from tests_data.contact_test_data import VALID_CONTACT_DATA, INVALID_CONTACT_DATA_WITH_EMPTY_FIELD, \
    EMAIL_INVALID_DATA_ADD_CONTACT


@pytest.mark.parametrize("contact", VALID_CONTACT_DATA)
def test_add_contact_success_all_fields(authenticated_driver, contact):
    add_contact_page = HomePage(authenticated_driver).open_add_contact_form()

    add_contact_page.fill_add_contact_form(contact)

    add_contact_page.wait_until_contact_add_form_closed()


@pytest.mark.parametrize("contact, expected_behavior, expected_message", INVALID_CONTACT_DATA_WITH_EMPTY_FIELD)
def test_add_contact_with_empty_field(authenticated_driver, contact, expected_behavior, expected_message):
    add_contact_page = HomePage(authenticated_driver).open_add_contact_form()
    add_contact_page.fill_add_contact_form(contact)

    if expected_behavior == "alert":
        try:
            actual_message = add_contact_page.get_alert_text()
        except TimeoutException:
            pytest.fail(f"Expected alert did not appear"
                        f"{expected_message!r}",
                        pytrace = False)



        assert expected_message in actual_message, (
        f"Expected message: {expected_message!r}, "
        f"actual message: {actual_message!r}")

        add_contact_page.alert_accept()

    elif expected_behavior == "Form_closed":
        assert  add_contact_page.wait_until_contact_add_form_closed()

@pytest.mark.parametrize("data", EMAIL_INVALID_DATA_ADD_CONTACT)
def test_add_contact_with_invalid_field_email(authenticated_driver, data):
    add_contact_page = HomePage(authenticated_driver).open_add_contact_form()
    add_contact_page.fill_add_contact_form(data)

    assert "Email not valid" in add_contact_page.get_alert_text()

    add_contact_page.alert_accept()
