from time import sleep

import pytest


from pages.home_page import HomePage
from tests_data.contact_test_data import VALID_CONTACT_DATA



@pytest.mark.parametrize("contact", VALID_CONTACT_DATA)
def test_add_contact_success_all_fields(authenticated_driver, contact):
    add_contact_page = HomePage(authenticated_driver).open_add_contact_form()

    add_contact_page.fill_add_contact_form(contact)

    add_contact_page.wait_until_contact_add_form_closed()
