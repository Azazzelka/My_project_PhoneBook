

import pytest

from pages.home_page import HomePage
from tests_data.edit_contact_test_data import VALID_EDIT_NAME_DATA, VALID_EDIT_LAST_NAME_DATA, VALID_EDIT_PHONE_DATA, \
    VALID_EDIT_EMAIL_DATA, VALID_EDIT_ADDRESS_DATA, VALID_EDIT_DESCRIPTION_DATA


@pytest.mark.parametrize("contact, new_name", VALID_EDIT_NAME_DATA)
def test_edit_contact_name_update(authenticated_driver, contact, new_name):
    add_contact_page = HomePage(authenticated_driver).open_add_contact_form()

    add_contact_page.fill_add_contact_form(contact)

    contacts_page = add_contact_page.open_contacts_page()

    contacts_page.edit_field_in_contacts_form_by_phone(contact.phone, contacts_page.EDIT_NAME_INPUT, new_name)
    contacts_page.get_contact_details_card_updated(contact.phone, new_name)

    assert contacts_page.get_contact_name_by_phone(contact.phone) == new_name

@pytest.mark.parametrize("contact, new_last_name", VALID_EDIT_LAST_NAME_DATA)
def test_edit_contact_last_name_update(authenticated_driver, contact, new_last_name):
    add_contact_page = HomePage(authenticated_driver).open_add_contact_form()

    add_contact_page.fill_add_contact_form(contact)

    contacts_page = add_contact_page.open_contacts_page()

    contacts_page.edit_field_in_contacts_form_by_phone(contact.phone, contacts_page.EDIT_LAST_NAME_INPUT, new_last_name)
    contacts_page.get_contact_details_card_updated(contact.phone, new_last_name)

    assert contacts_page.get_edit_contact_value(contacts_page.EDIT_LAST_NAME_INPUT) == new_last_name
@pytest.mark.parametrize("contact, new_phone", VALID_EDIT_PHONE_DATA)
def test_edit_contact_phone_update(authenticated_driver, contact, new_phone):
    add_contact_page = HomePage(authenticated_driver).open_add_contact_form()

    add_contact_page.fill_add_contact_form(contact)

    contacts_page = add_contact_page.open_contacts_page()

    contacts_page.edit_field_in_contacts_form_by_phone(contact.phone, contacts_page.EDIT_PHONE_INPUT, new_phone)
    contacts_page.get_contact_details_card_updated_by_name(contact.name, new_phone)

    assert contacts_page.get_edit_contact_value(contacts_page.EDIT_PHONE_INPUT) == new_phone

@pytest.mark.parametrize("contact, new_email", VALID_EDIT_EMAIL_DATA)
def test_edit_contact_email_update(authenticated_driver, contact, new_email):
    add_contact_page = HomePage(authenticated_driver).open_add_contact_form()

    add_contact_page.fill_add_contact_form(contact)

    contacts_page = add_contact_page.open_contacts_page()

    contacts_page.edit_field_in_contacts_form_by_phone(contact.phone, contacts_page.EDIT_EMAIL_INPUT, new_email)
    contacts_page.get_contact_details_card_updated(contact.phone, new_email)

    assert contacts_page.get_edit_contact_value(contacts_page.EDIT_EMAIL_INPUT) == new_email


@pytest.mark.parametrize("contact, new_address", VALID_EDIT_ADDRESS_DATA)
def test_edit_contact_address_update(authenticated_driver, contact, new_address):
    add_contact_page = HomePage(authenticated_driver).open_add_contact_form()

    add_contact_page.fill_add_contact_form(contact)

    contacts_page = add_contact_page.open_contacts_page()

    contacts_page.edit_field_in_contacts_form_by_phone(contact.phone, contacts_page.EDIT_ADDRESS_INPUT, new_address)
    contacts_page.get_contact_details_card_updated(contact.phone, new_address)

    assert contacts_page.get_edit_contact_value(contacts_page.EDIT_ADDRESS_INPUT) == new_address

@pytest.mark.skip(reason="Функциональность description пока не работает")
@pytest.mark.parametrize("contact, new_description", VALID_EDIT_DESCRIPTION_DATA)
def test_edit_contact_description_update(authenticated_driver, contact, new_description):
    add_contact_page = HomePage(authenticated_driver).open_add_contact_form()

    add_contact_page.fill_add_contact_form(contact)

    contacts_page = add_contact_page.open_contacts_page()

    contacts_page.edit_field_in_contacts_form_by_phone(contact.phone, contacts_page.EDIT_DESCRIPTION_INPUT, new_description)
    contacts_page.get_contact_details_card_updated(contact.phone, new_description)

    assert contacts_page.get_edit_contact_value(contacts_page.EDIT_DESCRIPTION_INPUT) == new_description


