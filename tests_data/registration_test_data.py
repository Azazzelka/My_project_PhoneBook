from models.registration_data import RegistrationData
from faker import Faker
from tests_data.login_test_data import create_valid_password

fake = Faker()

VALID_REGISTRATION_DATA = [
    RegistrationData(fake.unique.email(), create_valid_password())
    for _ in range(7)
]


INVALID_EMAIL_REGISTRATION_DATA = [
    RegistrationData("", "Valid123!"),              # T1, T2
    RegistrationData("   ", "Valid123!"),           # T2
    RegistrationData("annatest.com", "Valid123!"),  # T3: нет @
    RegistrationData("anna@@test.com", "Valid123!"),# T3: два @
    RegistrationData("@test.com", "Valid123!"),     # T4
    RegistrationData("anna@", "Valid123!"),         # T5
    RegistrationData("анна@test.com", "Valid123!"), # T6
    RegistrationData("anna@тест.com", "Valid123!"), # T6
]


INVALID_PASSWORD_REGISTRATION_DATA = [
    RegistrationData("Qanna@test.com", ""),          # T7, T8
    RegistrationData("Qanna@test.com", "        "),  # T8
    RegistrationData("Qanna@test.com", "Anna1234"),  # T9: нет спецсимвола
    RegistrationData("Qanna@test.com", "Anna123%"),  # T9: неверный спецсимвол
    RegistrationData("Qanna@test.com", "Анна123!"),  # T10
    RegistrationData("Qanna@test.com", "anna123!"),  # T11: нет UpperCase
    RegistrationData("Qanna@test.com", "ANNA123!"),  # T12: нет LowCase
    RegistrationData("Qanna@test.com", "AnnaTest!"), # T13: нет цифры
    RegistrationData("Qanna@test.com", "Ann1!aa"),   # T14: 7 символов
    RegistrationData(
        "Qanna@test.com",
        "AnnaTest12345!aa"
    ),                                               # T15: 16 символов
]