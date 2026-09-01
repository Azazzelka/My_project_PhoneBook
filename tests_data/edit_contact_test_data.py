
import pytest

from tests_data.contact_test_data import create_contact


VALID_EDIT_NAME_DATA = [
    pytest.param(
        create_contact(),
        "Micwhael",
        id="edit-name-latin",
    ),
    pytest.param(
        create_contact(),
        "Anneea Maria",
        id="edit-name-with-space",
    ),
    pytest.param(
        create_contact(),
        "Maeery-Jane",
        id="edit-name-with-hyphen",
    ),
    pytest.param(
        create_contact(),
        "Oee'Connor",
        id="edit-name-with-apostrophe",
    ),
    pytest.param(
        create_contact(),
        "Владqwимир",
        id="edit-name-cyrillic",
    ),
]

VALID_EDIT_LAST_NAME_DATA = [
    pytest.param(
        create_contact(),
        "Johnson",
        id="edit-last-name-latin",
    ),
    pytest.param(
        create_contact(),
        "Van Buren",
        id="edit-last-name-with-space",
    ),
    pytest.param(
        create_contact(),
        "Smith-Jones",
        id="edit-last-name-with-hyphen",
    ),
    pytest.param(
        create_contact(),
        "O'Connor",
        id="edit-last-name-with-apostrophe",
    ),
    pytest.param(
        create_contact(),
        "Иванов",
        id="edit-last-name-cyrillic",
    ),
]


VALID_EDIT_PHONE_DATA = [
    pytest.param(
        create_contact(),
        "0503234567",
        id="edit-phone-prefix-050",
    ),
    pytest.param(
        create_contact(),
        "0524345678",
        id="edit-phone-prefix-052",
    ),
    pytest.param(
        create_contact(),
        "0537456789",
        id="edit-phone-prefix-053",
    ),
    pytest.param(
        create_contact(),
        "0544567290",
        id="edit-phone-prefix-054",
    ),
    pytest.param(
        create_contact(),
        "0583678901",
        id="edit-phone-prefix-058",
    ),
]


VALID_EDIT_EMAIL_DATA = [
    pytest.param(
        create_contact(),
        "michael@example.com",
        id="edit-email-basic",
    ),
    pytest.param(
        create_contact(),
        "anna.maria@example.com",
        id="edit-email-with-dot",
    ),
    pytest.param(
        create_contact(),
        "user123@example.com",
        id="edit-email-with-digits",
    ),
    pytest.param(
        create_contact(),
        "user+phonebook@example.com",
        id="edit-email-with-plus",
    ),
    pytest.param(
        create_contact(),
        "user@mail.example.com",
        id="edit-email-with-subdomain",
    ),
]


VALID_EDIT_ADDRESS_DATA = [
    pytest.param(
        create_contact(),
        "15 King Street",
        id="edit-address-basic",
    ),
    pytest.param(
        create_contact(),
        "221B Baker Street, London",
        id="edit-address-with-letter",
    ),
    pytest.param(
        create_contact(),
        "25 Herzl St., Tel Aviv",
        id="edit-address-with-punctuation",
    ),
    pytest.param(
        create_contact(),
        "Apartment 12, 10 Main Road",
        id="edit-address-with-apartment",
    ),
    pytest.param(
        create_contact(),
        "ул. Пушкина, дом 10, кв. 5",
        id="edit-address-cyrillic",
    ),
]


VALID_EDIT_DESCRIPTION_DATA = [
    pytest.param(
        create_contact(),
        "Friend from work",
        id="edit-description-basic",
    ),
    pytest.param(
        create_contact(),
        "Call after 18:00.",
        id="edit-description-with-time",
    ),
    pytest.param(
        create_contact(),
        "Important contact: manager, sales department.",
        id="edit-description-with-punctuation",
    ),
    pytest.param(
        create_contact(),
        "Met in 2026 at the QA conference.",
        id="edit-description-with-digits",
    ),
    pytest.param(
        create_contact(),
        "Позвонить после работы.",
        id="edit-description-cyrillic",
    ),
]