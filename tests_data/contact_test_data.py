from dataclasses import replace

import pytest
from faker import Faker

from models.contact import Contact

fake = Faker()

VALID_CONTACT_DATA = [Contact(
    name= fake.unique.first_name(),
    last_name= fake.unique.last_name(),
    phone = fake.unique.numerify("##########"),
    email = fake.unique.email(),
    address = fake.unique.address(),
    description = fake.sentence()
)
    for _ in range(4)
]


def create_contact(**overrides) -> Contact:
    data = {
        "name": fake.first_name(),
        "last_name": fake.last_name(),
        "phone": fake.unique.numerify("05########"),
        "email": fake.unique.email(),
        "address": fake.address(),
        "description": fake.sentence(),
            }
    data.update(overrides)
    return Contact(**data)

INVALID_CONTACT_DATA_WITH_EMPTY_FIELD = [
    pytest.param(
        replace(create_contact(), name=""),
        "alert",
        "Name cannot be empty!",
        id = "empty-name",
    ),
    pytest.param(
        replace(create_contact(), last_name=""),
        "alert",
        "Last Name cannot be empty!",
        id = "empty-last-name",
    ),
    pytest.param(
        replace(create_contact(), phone=""),
        "alert",
        "Phone not valid",
        id = "empty-phone",
    ),
    pytest.param(
        replace(create_contact(), email=""),
        "alert",
        "Email not valid",
        id= "empty-email",
    ),
    pytest.param(
        replace(create_contact(), address=""),
        "alert",
        "Address cannot be empty!",
        id = "empty-address",
    ),
    pytest.param(
        replace(create_contact(), description=""),
        "Form_closed",
        None,
        id = "empty-description",
    )

]

