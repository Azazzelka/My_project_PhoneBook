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